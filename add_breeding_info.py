import flask, flask.views
import os
import sys
import utils
from flask_sqlalchemy import SQLAlchemy
from models import *
#import datetime

class add_breeding_info(flask.views.MethodView):
    
    db.create_all()
        
    @utils.login_required
    def get(self):

        strain_dict = {}
        strain_list = []

        __table__ = strain_info
        strains = __table__.query.order_by(__table__.Strain_id)

        for strain in strains:            
            strain_dict = dict((col,getattr(strain,col)) for col in strain.__table__.columns.keys())
            strain_list.append(strain_dict)

        mouse_dict = {}
        mouse_list = []

        __table__ = mice_list
        mice = __table__.query.order_by(__table__.Mouse_id)
        
        for mouse in mice:            
            mouse_dict = dict((col,getattr(mouse,col)) for col in mouse.__table__.columns.keys())
            mouse_list.append(mouse_dict)

        return flask.render_template('add_breeding_info.html', mice_list=mouse_list, mice_dict=mouse_dict, strain_list=strain_list, strain_dict=strain_dict)

#        return flask.render_template('add_breeding_info.html')
        
    @utils.login_required
    def post(self):

        pups_born_date = flask.request.form['datepupsborn']
        input1 = Breeding(  flask.request.form['bc'],
                            flask.request.form['mousetag'],
                            flask.request.form['dateofsetup'],
                            flask.request.form['pupstrain'],
                            flask.request.form['datepupsborn'],
                            datetime.date(*map(int, pups_born_date.split('-'))) + datetime.timedelta(days=21),
                            datetime.date(*map(int, pups_born_date.split('-'))) + datetime.timedelta(days=28))


        db.session.add(input1)
        db.session.commit()
        flask.flash("The Breeding info has been successfully added")
        return flask.redirect(flask.url_for('add_breeding_info'))        