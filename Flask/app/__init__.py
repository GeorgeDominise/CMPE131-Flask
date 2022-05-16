from flask import Flask

myobj_ = Flask(__name__)
myobj_.config.from_mapping(SECRET_KEY = 'George') #Needed in order to add cities above welcome message
#Without this, causes internal server error.
from app import routes