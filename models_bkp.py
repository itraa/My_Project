import flask,flask.views
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
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
    MAIL_USERNAME = 'itraa.narayan@gmail.com',
    MAIL_PASSWORD = 'ParupuRaghava1624')

#administrator list
ADMINS = ['itraa.narayan@gmail.com']
mail = Mail(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Breeding(db.Model):
    __tablename__ = 'Breeding'
    Breeding_Cage_Id = db.Column(db.String(100),primary_key=True)
    Male_Tag = db.Column(db.String(100))
    Male_DOB = db.Column(db.String(10))
    Female1_Tag = db.Column(db.String(100))
    Female1_DOB = db.Column(db.String(10))
    Female2_Tag = db.Column(db.String(100))
    Female2_DOB = db.Column(db.String(10))
    Date_Setup = db.Column(db.String(10))

    Male_Strain = db.Column(db.String(100),db.ForeignKey('strain_info.Strain_name'))
    Female_Strain = db.Column(db.String(100),db.ForeignKey('strain_info.Strain_name'))
    Offspring_Strain = db.Column(db.String(100),db.ForeignKey('strain_info.Strain_name'))
    strains = db.relationship('strain_info',backref='strain_ref')

#    Pups_cage_id = db.Column(db.String(100),db.ForeignKey('pups_info.Breeding_Cage_Id'))
#    Date_Pups_Born = db.Column(db.String(10))
#    First_Date_of_weaning = db.Column(db.String(10))
#    Final_Date_of_weaning = db.Column(db.String(10))

    def __init__(self,Breeding_Cage_Id,Male_Tag,Male_DOB,Female1_Tag,Female1_DOB,Female2_Tag,Female2_DOB,Date_Setup,Male_Strain,Female_Strain,Offspring_Strain):
        self.Breeding_Cage_Id = Breeding_Cage_Id
        self.Male_Tag = Male_Tag
        self.Male_DOB = Male_DOB
        self.Female1_Tag = Female1_Tag
        self.Female1_DOB = Female1_DOB
        self.Female2_Tag = Female2_Tag
        self.Female2_DOB = Female2_DOB
        self.Date_Setup = Date_Setup
        self.Male_Strain = Male_Strain
        self.Female_Strain = Female_Strain
        self.Offspring_Strain = Offspring_Strain

#        self.Pups_cage_id = Pups_cage_id
#        self.Date_Pups_Born = Date_Pups_Born
#        self.First_Date_of_weaning = First_Date_of_weaning
#        self.Final_Date_of_weaning = Final_Date_of_weaning

    def __repr__(self):
        return "<Breeding(%s, %s, %s, %s, %s, %s, %s, %s>" % (self.Breeding_Cage_Id, self.Male_Tag, self.Male_DOB, self.Female1_Tag, self.Female1_DOB,
            self.Female2_Tag, self.Female2_DOB, self.Date_Setup,self.Male_Strain,self.Female_Strain,self.Offspring_Strain)

class pups_info(db.Model):
#    __tablename__ = 'pups_info'
    Pups_info_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    Date_Pups_Born = db.Column(db.String(10))
    First_Date_of_weaning = db.Column(db.String(10))
    Final_Date_of_weaning = db.Column(db.String(10))

    Pups_Breeding_Cage_Id = db.Column(db.String(100),db.ForeignKey('Breeding.Breeding_Cage_Id'))
    pups = db.relationship('Breeding',backref='birth')

    def __init__(self,Pups_Breeding_Cage_Id,Date_Pups_Born,First_Date_of_weaning,Final_Date_of_weaning):
# No autoincremented field in the init as it will be created by the db.
#        self.Pups_info_id = Pups_info_id
        self.Pups_Breeding_Cage_Id = Pups_Breeding_Cage_Id
        self.Date_Pups_Born = Date_Pups_Born
        self.First_Date_of_weaning = First_Date_of_weaning
        self.Final_Date_of_weaning = Final_Date_of_weaning

    def __repr__(self):
        return "<pups_info(%d, %s, %s, %s, %s>" % (self.Pups_info_id, self.Pups_Breeding_Cage_Id, self.Date_Pups_Born, self.First_Date_of_weaning, 
            self.Final_Date_of_weaning)

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
    Cage_id = db.Column(db.String(100),primary_key=True)
    Date_created = db.Column(db.String(10))
    Cage_cost = db.Column(db.Integer)
    Mouse_id = db.Column(db.String(100))
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

    def __init__(self,Cage_id,Date_created,Cage_cost,Mouse_id,Gender,Date_of_birth,Date_of_weaning,Age,Status,Breeding_cage_origin,Mouse_strain_name,Use,Date_removed,Death_info,Notes):
        self.Cage_id = Cage_id
        self.Date_created = Date_created
        self.Cage_cost = Cage_cost
        self.Mouse_id = Mouse_id
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
        return "<strain_info(%s, %s, %d, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s>" % (self.Cage_id,self.Date_created,self.Cage_cost,self.Mouse_id,self.Gender,
            self.Date_of_birth,self.Date_of_weaning,self.Age,self.Status,self.Breeding_cage_origin,self.Mouse_strain_name,self.Use,self.Date_removed,self.Death_info,self.Notes)

