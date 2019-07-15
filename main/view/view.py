from . import view_bp
import hashlib
from flask import render_template
from flask import request
from flask import send_from_directory


@view_bp.route("/")
def home_view():
    return render_template("home.html")

@view_bp.route("/articles")
def articles():
    return render_template("articles.html")

