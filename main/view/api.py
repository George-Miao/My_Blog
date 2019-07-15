from flask import Blueprint
from flask import request
from flask import jsonify
from . import connect
from . import api_bp
import json


@api_bp.route("/zapier_post", methods=['POST'])
def zapier():
    req = request
    print(req.get_json())
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@api_bp.route("/dropbox_post", methods=['GET', 'POST'])
def webhook():
    print("New Edit")
    req = request
    if "challenge" in req.args:
        print("New challenge: " + req.args['challenge'])
        return req.args['challenge']
    json = req.get_json()
    print(json)
    return "0"

@api_bp.route("/content")
def get_content():
    article_id = int(request.args['id'])
    return jsonify(connect.get_article_by_id(article_id))