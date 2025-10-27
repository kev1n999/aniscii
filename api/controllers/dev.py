from ..resources.generate_ascii import ascii_generator
from flask import Response 
from ..gif_paths import gif_paths

DEV = gif_paths["dev"]

def dev_ascii():
  def frames():
    for frame in ascii_generator("dev", DEV):
      yield f"\033[2J\033[H{frame}\n"
  
  return Response(frames(), mimetype="text/event-stream")