from flask import Flask 
#from the file config.py, import the class Config
from config import Config

app = Flask(__name__)
'''
configuration could also be hardcoded here,
I opted to put it in it's own file 'config.py'
app.config['SECRET_KEY']='place-holder-pass
'''
app.config.from_object(Config)

from app import routes