from flask import Blueprint

controller = Blueprint('con', __name__, url_prefix="/api")

from . import content_controller