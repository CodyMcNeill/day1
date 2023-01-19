import os

basedir = os.path.abspath(os.path.dirname(__name__))

class Config():
    FLASK_APP = 'run.py'
    FLASK_ENV = 'development'