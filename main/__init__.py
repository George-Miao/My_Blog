from flask import Flask
from .view import view
from .controller import controller_bp
from os.path import dirname, join

app = Flask(__name__)

app.register_blueprint(view)
app.register_blueprint(controller_bp)

@app.errorhandler(404)
def e404(e):
    return '''404:
    Cannot find the page you are looking for
    '''


