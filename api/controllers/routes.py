import json 
from flask import Response
from ..gif_paths import gif_paths

def get_routes():
  data = {key: f"/{key}" for key in gif_paths.keys()}

  return Response(
    json.dumps(data, indent=2),
    mimetype="application/json"
  )