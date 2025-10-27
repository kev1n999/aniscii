from ..resources.generate_ascii import ascii_generator
from flask import Response 
from ..gif_paths import gif_paths

MUSK = gif_paths["musk"]

def musk_ascii():
  def frames():
    for frame in ascii_generator("musk", MUSK):
      yield f"\033[2J\033[H{frame}\n"
  
  return Response(frames(), mimetype="text/event-stream")