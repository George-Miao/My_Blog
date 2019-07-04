from . import controller
from flask import request


@controller.route("/content")
def get_content():
    number = request.args['number']
    id = request.args['id']
    return ""
