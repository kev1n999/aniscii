from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .resources.generate_ascii import ascii_generator
from .routes.main import main 

def create_app():
  app = Flask(__name__, static_folder="static", template_folder="static")
  limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["10 per minute"],
  )
  
  app.register_blueprint(main)

  return app 