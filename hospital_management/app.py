
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__) #_name_tells you where the app is located
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db' #database location
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #avoids warning messages 
db = SQLAlchemy(app) #initialize the database 

#--------------------MODELS-------------------

from datetime import datetime
class User(db.Model):
    __tablename__ = 'USERS' #table name in database
    user_id = db.Column(db.Integer, primary_key=True) #primary key
    specialization_id = db.Column(db.Integer, db.ForeignKey('DEPARTMENTS.department_id'), nullable=True)
    username = db.Column(db.String(100), unique=True, nullable=False) #nullable means it must be filled(mandatory field)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50),nullable=False)
    role = db.Column(db.String(20),nullable=False) #roles like Admin, Doctor , Patient
    created_at = db.Column(db.DateTime, default=datetime.utcnow) #This will store date and time of user when he is creating account
 #reverse relationship between User and Department
    department = db.relationship('Department', back_populates='doctors')

class Department(db.Model):
    __tablename__= 'DEPARTMENTS'
    department_id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    doctors = db.relationship('User', back_populates='department')

class Treatment(db.Model):
    __tablename__ = 'TREATMENTS'
    treatment_id = db.Column(db.Integer,primary_key=True)
    treat_name = db.Column(db.String(100))
    description = db.Column(db.Text, nullable=True)

class Appointment(db.Model):
    __tablename__ = 'APPOINTMENTS'
    Appointment_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), default='Scheduled') #Scheduled, Completed, Canceled
    #connection with user table
    user_id = db.Column(db.Integer,db.ForeignKey('USERS.user_id'))
    treatment_id = db.Column(db.Integer, db.ForeignKey('TREATMENTS.treatment_id'), nullable=False)



    #Run the app and create database
if __name__=='__main__':
        with app.app_context():    #Needed for the DB Operation
            db.create_all()        #Create the database and tables
            existing_admin = User.query.filter_by(username="admin").first()
            if not existing_admin:
             admin_db = User(
                 username ="admin",
                 password = "ad123",
                 email = "admin@example.com",
                 role = "admin"
                )
             db.session.add(admin_db)
             db.session.commit()
        app.run(debug=True)