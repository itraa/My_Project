import flask,flask.views
import settings
import os
import utils
from flask_sqlalchemy import SQLAlchemy
from main import Main
from login import Login
#from search_breeding_info import *
from music import Music
#from models import *
from datetime import *
from flask import jsonify
import json

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
app.secret_key =  settings.secret_key
main_view_func = Main.as_view('main')

def to_json(inst, cls):
    """
    Jsonify the sql alchemy query result.
    """
    convert = dict()
    # add your coversions for things like datetime's 
    # and what-not that aren't serializable.
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type in convert.keys() and v is not None:
            try:
                d[c.name] = convert[c.type](v)
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return json.dumps(d)

class Breeding(db.Model):
    Breeding_Cage_Id = db.Column(db.String(100),primary_key=True,unique=True)
    Male_Tag = db.Column(db.String(100))
    Male_DOB = db.Column(db.String)
    Female1_Tag = db.Column(db.String(100))
    Female1_DOB = db.Column(db.String)
    Female2_Tag = db.Column(db.String(100))
    Female2_DOB = db.Column(db.String)
    Date_Setup = db.Column(db.String)
    Date_Pups_Born = db.Column(db.String)

    def __init__(self,Breeding_Cage_Id,Male_Tag,Male_DOB,Female1_Tag,Female1_DOB,Female2_Tag,Female2_DOB,Date_Setup,Date_Pups_Born):
        self.Breeding_Cage_Id = [Breeding_Cage_Id]
        self.Male_Tag = [Male_Tag]
        self.Male_DOB = [Male_DOB]
        self.Female1_Tag = [Female1_Tag]
        self.Female1_DOB = [Female1_DOB]
        self.Female2_Tag = [Female2_Tag]
        self.Female2_DOB = [Female2_DOB]
        self.Date_Setup = [Date_Setup]
        self.Date_Pups_Born = [Date_Pups_Born]

    def __repr__(self):
        return "<Breeding(%s, %s, %s, %s, %s, %s, %s, %s, %s'>" % (self.Breeding_Cage_Id, self.Male_Tag, self.Male_DOB, self.Female1_Tag, self.Female1_DOB,
            self.Female2_Tag, self.Female2_DOB, self.Date_Setup, self.Date_Pups_Born)           

    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'Breeding_Cage_Id': [self.Breeding_Cage_Id],
           'Male_Tag': [self.Male_Tag],
           'Male_DOB': [self.Male_DOB],
           'Female1_Tag': [self.Female1_Tag],
           'Female1_DOB': [self.Female1_DOB],
           'Female2_Tag': [self.Female2_Tag],
           'Female2_DOB': [self.Female2_DOB],
           'Date_Setup': [self.Date_Setup],
           'Date_Pups_Born': [self.Date_Pups_Born]
                }


class add_breeding_info(flask.views.MethodView):
    
    db.create_all()

    @utils.login_required
    def get(self):
        return flask.render_template('add_breeding_info.html')
        
    @utils.login_required
    def post(self):
        input = Breeding(flask.request.form['bc'],
                           flask.request.form['maletag'],
                            flask.request.form['maledob'],
                            flask.request.form['female1tag'],
                            flask.request.form['female1dob'],
                            flask.request.form['female2tag'],
                            flask.request.form['female2dob'],
                            flask.request.form['dateofsetup'],
                            flask.request.form['datepupsborn'])
        db.session.add(input)
        db.session.commit()
        flask.flash("The Breeding info has been successfully added")
        return flask.redirect(flask.url_for('search_breeding_info'))

class search_breeding_info(flask.views.MethodView):

#    def json(self):
#        return to_json(self, self.__class__)
    __table__ = Breeding

    @utils.login_required
    def get(self):
        return flask.render_template('search_breeding_info.html')

    @utils.login_required
    def post(self):
        item = flask.request.form['bc']
        search = Breeding.query.filter_by(Breeding_Cage_Id = item).first()
        flask.flash(search)
#        search_dict = dict((col,getattr(Breeding,col)) for col in Breeding.__table__.columns.keys())
        return flask.render_template('search_breeding_info.html',
            item = item,
            search = search)        
#        search = Breeding.query.get(item)
#        search_json = json.dumps(search.__dict__)
#        search_serial = jsonify(json_list=[i.serialize for i in search.all()])
#        search_serial = jsonify(json_list=search.all())
#        search_serial = to_json(self, self.__class__)
#        flask.flash(search_serial)
#        return flask.redirect(flask.url_for('search_breeding_info'))

# Routes
app.add_url_rule('/',
                 view_func=main_view_func,
                 methods=["GET"])
app.add_url_rule('/<page>/',
                 view_func=main_view_func,
                 methods=["GET"])
app.add_url_rule('/login/',
                 view_func=Login.as_view('login'),
                 methods=["GET", "POST"])

app.add_url_rule('/add_breeding_info/',
                view_func=add_breeding_info.as_view('add_breeding_info'), 
                methods=['GET','POST'])

app.add_url_rule('/search_breeding_info/',
                view_func=search_breeding_info.as_view('search_breeding_info'), 
                methods=['GET','POST'])

@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('404.html'), 404

app.debug = True
use_reloader=False
app.run()
""