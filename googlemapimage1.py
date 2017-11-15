#geo map code into flask
from flask import flask, rendertemplate
from flask.ext.googlemaps import Googlemaps
app = Flask(foodprint)
Googlemaps(app)
