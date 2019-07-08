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

@view.route("/webhook", methods=['GET', 'POST'])
def webhook():
    a = request.args
    return '1'
