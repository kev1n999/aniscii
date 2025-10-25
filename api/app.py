import os 
from flask import Flask, Request, Response, json 
from dotenv import load_dotenv
from .resources.generate_ascii import ascii_generator
from .routes.main import main 

load_dotenv()

def create_app():
  app = Flask(__name__)
  app.register_blueprint(main)

  return app 