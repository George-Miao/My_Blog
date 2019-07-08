from . import view
from flask import render_template
from flask import request
from flask import send_from_directory


@view.route("/")
def home_view():
    return render_template("home.html")

@view.route("/articles")
def articles():
    return "articles"

#SSL verification
@view.route("/.well-known/pki-validation/<path:filename>")
def verification(filename):
    return send_from_directory("static/file", filename, as_attachment=True)