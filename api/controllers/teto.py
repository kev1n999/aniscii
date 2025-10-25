from ..resources.generate_ascii import ascii_generator
from flask import Response 
from ..gif_paths import gif_paths

TETO = gif_paths["teto"]

def teto_ascii():
  def frames():
    for frame in ascii_generator("teto", TETO):
      yield f"\033[2J\033[H{frame}\n"
  
  return Response(frames(), mimetype="text/event-stream")