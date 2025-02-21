'''
This file isn't necessary now, since cursd-blog is
so simple, but configurations become important later.
As it stands, this file holds a class that contains variables
that are defined as keys.
SECRET_KEY is a variable used to prevent cross-site request forgery
'''
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'place-holder-pass-key-should-change-later'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')