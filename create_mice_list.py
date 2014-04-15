import flask, flask.views
import os
import sys
import utils
from datetime import date
import datetime
from flask_sqlalchemy import SQLAlchemy
from models import *

class create_mice_list(flask.views.MethodView):
    
        
    @utils.login_required
    def get(self):
        search_dict = {}
        search_list = []

        __table__ = strain_info
        search = __table__.query.order_by(__table__.Strain_id)

        for result in search:            
            search_dict = dict((col,getattr(result,col)) for col in result.__table__.columns.keys())
            search_list.append(search_dict)
        return flask.render_template('create_mice_list.html', search_list=search_list, search_dict=search_dict)
#        return flask.render_template('create_mice_list.html')
        
    @utils.login_required
    def post(self):

        date_format = "%Y-%m-%d"
        today = date.today()
        birth_date = flask.request.form['dateofbirth']
        born = datetime.datetime.strptime(birth_date,date_format)
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

#datetime.date(*map(int, pups_born_date.split('-'))) + datetime.timedelta(days=21)
#        date_format = "%Y-%m-%d"
#        birth_date = flask.request.form['dateofbirth']
#        start = datetime.strptime(birth_date,date_format)
#        end = datetime.strptime(str(date.today()),date_format)
        
        input = mice_list(flask.request.form['mouseid'],
                            flask.request.form['cageid'],
                            flask.request.form['datecreated'],
                            flask.request.form['cagecost'],
                            flask.request.form['gender'],
                            flask.request.form['dateofbirth'],
                            flask.request.form['dateofweaning'],
#                            flask.request.form['age'],
                            age,   
#                            (date.today() - date(*map(int, birth_date.split('-')))).days,
                            flask.request.form['status'],
                            flask.request.form['bcorigin'],
                            flask.request.form['strain'],
                            flask.request.form['use'],
                            flask.request.form['dateremoved'],
                            flask.request.form['death'],
                            flask.request.form['notes']
                            )

        db.session.add(input)
        db.session.commit()
        flask.flash("The mice info has been successfully added")
        return flask.redirect(flask.url_for('create_mice_list'))        