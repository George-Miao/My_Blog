from flask import Blueprint
from ..service.redis_service_module import redis_service
from pathlib import Path

base_path = Path(__file__).parent
json_path = (base_path / "../static/file/redis.json").resolve()

connect = redis_service()
connect.load_json(json_path)
connect.connect()

controller_bp = Blueprint('controller', __name__, url_prefix="/api")

from . import content_controller