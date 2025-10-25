from ..resources.generate_ascii import ascii_generator
from flask import Response 
from ..gif_paths import gif_paths

PALMEIRAS = gif_paths["palmeiras"]

def palmeiras_ascii():
  def frames():
    for frame in ascii_generator("palmeiras", PALMEIRAS):
      yield f"\033[2J\033[H{frame}\n"
  
  return Response(frames(), mimetype="text/event-stream")