from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api
import os

MONGO_URI = "mongodb+srv://ugo:KKKyl.011@cluster0.bux3b.mongodb.net/slumbook?retryWrites=true&w=majority"

# Initialize application
app = Flask(__name__, static_folder='static', template_folder='templates')

# #Initialize Flask PyMongo
mongo = PyMongo(app,MONGO_URI)

app.config['SECRET_KEY'] = '\x1c\x9e*\x1cO\xa3\xd26\xe9\xf6y\xae/n"\x83\xb2jiA\x9b\xec\xd5\xb0'

#initialize RESTful
api = Api(app)

# Import the application
from . import backview, views, google_auth
# from . import google_auth