from flask import Blueprint
from .. import db

'''
base_path = Path(__file__).parent
json_path = (base_path / "../static/file/redis.json").resolve()

connect = Redis_service()
connect.load_json(json_path)
connect.connect()
'''
view_bp = Blueprint('view', __name__)
api_bp = Blueprint('api', __name__, url_prefix="/api")

from . import api
from . import view
