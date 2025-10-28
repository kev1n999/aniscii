from flask import Blueprint, render_template
from ..controllers.teto import teto_ascii
from ..controllers.palmeiras import palmeiras_ascii
from ..controllers.batman import batman_ascii
from ..controllers.dev import dev_ascii
from ..controllers.musk import musk_ascii 
from ..controllers.routes import get_routes 

main = Blueprint("main", __name__)

@main.route("/")
def home():
  return render_template("index.html")

@main.route("/routes", methods=["GET"])
def routes():
  return get_routes()
  
@main.route("/teto", methods=["GET"])
def teto():
  return teto_ascii()

@main.route("/palmeiras", methods=["GET"])
def palmeiras():
  return palmeiras_ascii()

@main.route("/batman", methods=["GET"])
def batman():
  return batman_ascii()

@main.route("/dev", methods=["GET"])
def dev():
  return dev_ascii()

@main.route("/musk", methods=["GET"])
def musk():
  return musk_ascii()