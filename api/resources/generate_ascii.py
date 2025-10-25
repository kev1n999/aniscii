from PIL import Image, ImageSequence
import os
import time

chars = "@%#*+=-:$"

def resize_frame(frame, new_width=80):
    width, height = frame.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    return frame.resize((new_width, new_height))

def frame_to_ascii(frame):
    gray = frame.convert("L")  
    pixels = list(gray.getdata())
    ascii_str = ""
    for pixel in pixels:
        index = pixel * (len(chars) - 1) // 255
        ascii_str += chars[index]
    width = gray.width
    return "\n".join([ascii_str[i:i+width] for i in range(0, len(ascii_str), width)])

def ascii_generator(route: str, gif_path: str, time=50):
    img = Image.open(gif_path)
    frames = [resize_frame(frame.copy()) for frame in ImageSequence.Iterator(img)]
    ascii_frames = [frame_to_ascii(frame) for frame in frames]

    for x in range(time):
        for ascii_frame in ascii_frames:
            yield ascii_frame
            time.sleep(0.1) 