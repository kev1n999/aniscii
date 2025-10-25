from flask import Blueprint, render_template
from ..controllers.teto import teto_ascii

main = Blueprint("main", __name__)

@main.route("/")
def home():
  return render_template("index.html")

@main.route("/teto", methods=["GET"])
def teto():
  return teto_ascii()