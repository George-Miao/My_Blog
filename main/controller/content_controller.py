from flask import request
from flask import jsonify
from . import controller_bp
from . import connect

class RedisError(Exception):
    pass

@controller_bp.route("/content")
def get_content():
    article_id = int(request.args['id'])
    return jsonify(connect.get_article_by_id(article_id))

