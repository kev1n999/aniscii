from flask import Blueprint, render_template
from ..controllers.teto import teto_ascii
from ..controllers.palmeiras import palmeiras_ascii

main = Blueprint("main", __name__)

@main.route("/")
def home():
  return render_template("index.html")

@main.route("/teto", methods=["GET"])
def teto():
  return teto_ascii()

@main.route("/palmeiras", methods=["GET"])
def palmeiras():
  return palmeiras_ascii()