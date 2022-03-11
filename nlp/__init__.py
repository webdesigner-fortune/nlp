import os

from flask import Flask, render_template
from os.path import join, dirname, realpath
from flask_sqlalchemy import SQLAlchemy

################
#### config ####
################
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/upload/')
app.config['UPLOADED_PHOTOS_DEST'] = UPLOADS_PATH
db = SQLAlchemy(app)
####################
#### Database ####
####################
from nlp.models.Books import Books
from nlp.models.Search import Search
####################
#### blueprints ####
####################

from nlp.route import main_landing
app.register_blueprint(main_landing.bp)