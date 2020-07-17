from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)
app.config.from_object('config')
app.config["Debug"] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)

from GraphAppcn import views, models