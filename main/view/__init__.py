from flask import Blueprint

view = Blueprint('view', __name__)

from . import error_handler
from . import home
