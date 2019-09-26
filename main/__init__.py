from flask import Flask
from flask_cache import Cache

app = Flask(__name__)

app.jinja_env.variable_start_string = '[['
app.jinja_env.variable_end_string = ' ]]'

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

from .service import *

db = DBService('mlGGIlyepMAAAAAAAAAAPl_aW8lMTqNuy0ej2f9vdLS7wAurbkIpaYqEcMMRlAFJ')

from .view import view_bp
from .view import api_bp

app.register_blueprint(view_bp)
app.register_blueprint(api_bp)

@app.errorhandler(404)
def e404(e):
    return '''404:
    Cannot find the page you are looking for
    '''


