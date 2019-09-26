from flask import request, jsonify
from . import api_bp
from . import db
import datetime


@api_bp.route("/content")
def get_content():
    path = request.args['path']
    return db.request_file(path)


@api_bp.route("/list")
def get_count():
    return jsonify(db.request_list())


@api_bp.route("/db_wh")
def db_wh():
    if 'challenge' in request.args:
        return request.args['challenge']
    else:
        print('[+] Nice')