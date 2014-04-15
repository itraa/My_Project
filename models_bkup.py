import flask,flask.views
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from flask.ext.mail import Mail
#from config import *
# email server

app = flask.Flask(__name__)
mail = Mail(app)
app.config.update(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'itraa.narayan@gmail.com',
    MAIL_PASSWORD = 'ParupuRaghava1624')

#administrator list
ADMINS = ['itraa.narayan@gmail.com']
mail = Mail(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Breeding(db.Model):
    Breeding_Cage_Id = db.Column(db.String(100),primary_key=True,unique=True)
    Male_Tag = db.Column(db.String(100))
    Male_DOB = db.Column(db.String(10))
    Female1_Tag = db.Column(db.String(100))
    Female1_DOB = db.Column(db.String(10))
    Female2_Tag = db.Column(db.String(100))
    Female2_DOB = db.Column(db.String(10))
    Date_Setup = db.Column(db.String(10))
    Date_Pups_Born = db.Column(db.String(10))
    First_Date_of_weaning = db.Column(db.String(10))
    Final_Date_of_weaning = db.Column(db.String(10))

    def __init__(self,Breeding_Cage_Id,Male_Tag,Male_DOB,Female1_Tag,Female1_DOB,Female2_Tag,Female2_DOB,Date_Setup,Date_Pups_Born,First_Date_of_weaning,Final_Date_of_weaning):
        self.Breeding_Cage_Id = Breeding_Cage_Id
        self.Male_Tag = Male_Tag
        self.Male_DOB = Male_DOB
        self.Female1_Tag = Female1_Tag
        self.Female1_DOB = Female1_DOB
        self.Female2_Tag = Female2_Tag
        self.Female2_DOB = Female2_DOB
        self.Date_Setup = Date_Setup
        self.Date_Pups_Born = Date_Pups_Born
        self.First_Date_of_weaning = First_Date_of_weaning
        self.Final_Date_of_weaning = Final_Date_of_weaning

    def __repr__(self):
        return "<Breeding(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'>" % (self.Breeding_Cage_Id, self.Male_Tag, self.Male_DOB, self.Female1_Tag, self.Female1_DOB,
            self.Female2_Tag, self.Female2_DOB, self.Date_Setup, self.Date_Pups_Born, self.First_Date_of_weaning, self.Final_Date_of_weaning)

