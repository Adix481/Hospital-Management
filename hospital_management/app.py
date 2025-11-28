
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__) #_name_tells you where the app is located
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
