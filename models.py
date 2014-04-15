import flask,flask.views
import os
from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime, date
from flask.ext.mail import Mail
#from config import *
# email server

app = flask.Flask(__name__)
app.config.update(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'xxxx',
    MAIL_PASSWORD = 'xxxx')

#administrator list
ADMINS = ['xxxx']
mail = Mail(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Breeding(db.Model):
    __tablename__ = 'Breeding'
    Breeding_info_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    Breeding_Cage_Id = db.Column(db.String(100))
    Mouse_Tag = db.Column(db.String(100))
    Date_Setup = db.Column(db.String(10))
    Pups_strain = db.Column(db.String(100))
    Date_Pups_Born = db.Column(db.String(10))
    First_Date_of_weaning = db.Column(db.String(10))
    Final_Date_of_weaning = db.Column(db.String(10))

    Pups_strain = db.Column(db.String(100),db.ForeignKey('strain_info.Strain_name'))
    strains = db.relationship('strain_info',backref='strain_ref')

    def __init__(self,Breeding_Cage_Id,Mouse_Tag,Date_Setup,Pups_strain,Date_Pups_Born,First_Date_of_weaning,Final_Date_of_weaning):
# No autoincremented field in the init as it will be created by the db.
#        self.Breeding_info_id = Breeding_info_id
        self.Breeding_Cage_Id = Breeding_Cage_Id
        self.Mouse_Tag = Mouse_Tag
        self.Date_Setup = Date_Setup
        self.Pups_strain = Pups_strain
        self.Date_Pups_Born = Date_Pups_Born
        self.First_Date_of_weaning = First_Date_of_weaning
        self.Final_Date_of_weaning = Final_Date_of_weaning
 
    def __repr__(self):
        return "<Breeding(%d, %s, %s, %s, %s, %s, %s, %s>" % (self.Breeding_info_id, self.Breeding_Cage_Id, self.Mouse_Tag, self.Date_Setup,self.Pups_strain,self.Date_Pups_Born, self.First_Date_of_weaning, 
            self.Final_Date_of_weaning)

#class pups_info(db.Model):
#    __tablename__ = 'pups_info'
#    Pups_info_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#   Date_Pups_Born = db.Column(db.String(10))
#    First_Date_of_weaning = db.Column(db.String(10))
#    Final_Date_of_weaning = db.Column(db.String(10))

#    Pups_Breeding_Cage_Id = db.Column(db.String(100),db.ForeignKey('Breeding.Breeding_Cage_Id'))
#    pups = db.relationship('Breeding',backref='birth')

#    Pups_strain = db.Column(db.String(100),db.ForeignKey('strain_info.Strain_name'))
#    strains = db.relationship('strain_info',backref='strain_ref')

#    def __init__(self,Pups_Breeding_Cage_Id,Pups_strain,Date_Pups_Born,First_Date_of_weaning,Final_Date_of_weaning):
# No autoincremented field in the init as it will be created by the db.
#        self.Pups_info_id = Pups_info_id
#        self.Pups_Breeding_Cage_Id = Pups_Breeding_Cage_Id
#        self.Pups_strain = Pups_strain
#        self.Date_Pups_Born = Date_Pups_Born
#        self.First_Date_of_weaning = First_Date_of_weaning
#        self.Final_Date_of_weaning = Final_Date_of_weaning

#    def __repr__(self):
#        return "<pups_info(%d, %s, %s, %s, %s, %s>" % (self.Pups_info_id, self.Pups_Breeding_Cage_Id, self.Pups_strain,self.Date_Pups_Born, self.First_Date_of_weaning, 
#            self.Final_Date_of_weaning)

class strain_info(db.Model):
#    __tablename__ = 'strain_info'
    Strain_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    Strain_name = db.Column(db.String(100))
    Genetic_background = db.Column(db.String(100))
    Coat_color = db.Column(db.String(100))
    Strain_description = db.Column(db.String(250))
    Strain_source = db.Column(db.String(100))
    Source_description = db.Column(db.String(250))


    def __init__(self,Strain_name,Genetic_background,Coat_color,Strain_description,Strain_source,Source_description):
# No autoincremented field in the init as it will be created by the db.
#        self.Strain_Id = Strain_Id
        self.Strain_name = Strain_name
        self.Genetic_background = Genetic_background
        self.Coat_color = Coat_color
        self.Strain_description = Strain_description
        self.Strain_source = Strain_source
        self.Source_description = Source_description

    def __repr__(self):
        return "<strain_info(%d, %s, %s, %s, %s, %s, %s>" % (self.Strain_Id,self.Strain_name,self.Genetic_background,self.Coat_color,self.Strain_description,
            self.Strain_source,self.Source_description)


class mice_list(db.Model):
#    __tablename__ = 'strain_info'
#    Mice_list_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    Mouse_id = db.Column(db.String(100),primary_key=True)
    Cage_id = db.Column(db.String(100))
    Date_created = db.Column(db.String(10),primary_key=True)
    Cage_cost = db.Column(db.Integer)
    Gender = db.Column(db.String(6))
    Date_of_birth = db.Column(db.String(10))
    Date_of_weaning = db.Column(db.String(10))
    Age = db.Column(db.String(50))
    Status = db.Column(db.String(100))
    Use = db.Column(db.String(20))
    Date_removed = db.Column(db.String(10))
    Death_info = db.Column(db.String(100))
    Notes = db.Column(db.String(250))

    Breeding_cage_origin = db.Column(db.String(100),db.ForeignKey('Breeding.Breeding_Cage_Id'))
    breeding_origin = db.relationship('Breeding',backref='bday')

    Mouse_strain_name = db.Column(db.String(100),db.ForeignKey('strain_info.Strain_name'))
    mice_strain = db.relationship('strain_info',backref='strain')

    def __init__(self,Mouse_id,Cage_id,Date_created,Cage_cost,Gender,Date_of_birth,Date_of_weaning,Age,Status,Breeding_cage_origin,Mouse_strain_name,Use,Date_removed,Death_info,Notes):
        
        self.Mouse_id = Mouse_id
        self.Cage_id = Cage_id
        self.Date_created = Date_created
        self.Cage_cost = Cage_cost
        self.Gender = Gender
        self.Date_of_birth = Date_of_birth
        self.Date_of_weaning = Date_of_weaning
        self.Age = Age
        self.Status = Status
        self.Breeding_cage_origin = Breeding_cage_origin
        self.Mouse_strain_name = Mouse_strain_name
        self.Use = Use
        self.Date_removed = Date_removed
        self.Death_info = Death_info
        self.Notes = Notes

    def __repr__(self):
        return "<mice_list(%s, %s>" % (self.Mouse_id,self.Cage_id,self.Date_created,self.Cage_cost,self.Gender,self.Date_of_birth,self.Date_of_weaning,self.Age,self.Status,
            Breeding_cage_origin,self.Mouse_strain_name,self.Use,self.Date_removed,self.Death_info,self.Notes)

