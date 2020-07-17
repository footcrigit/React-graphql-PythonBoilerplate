import os

DBNAME = 'reactpythondb'
HOST = 'localhost'
DBUSER = 'devuser'
DBPWD = 'local123'

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://' + DBUSER + ':' + DBPWD + '@' + HOST + '/' + DBNAME
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = None
