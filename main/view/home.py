from . import view
from flask import render_template


@view.route("/")
def home_view():
    return render_template("home.html")

@view.route("/articles")
def articles():
    return "articles"
