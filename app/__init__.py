from flask import Flask 
#from the file config.py, import the class Config
from config import Config
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 


app = Flask(__name__)
'''
configuration could also be hardcoded here,
I opted to put it in it's own file 'config.py'
app.config['SECRET_KEY']='place-holder-pass
'''
app.config.from_object(Config)

'''
for sqlalchemy and flask-migrate
'''
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models