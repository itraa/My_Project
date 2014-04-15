import flask, flask.views
import os
import sys
import utils
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

#datetime.date(*map(int, pups_born_date.split('-'))) + datetime.timedelta(days=21)

#        mouse_birth_date = flask.request.form['date_of_birth']
#        date_format = "%Y-%m-%d"
#        birth_date = flask.request.form['dateofbirth']
        birth_date = "2013-12-24"
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
#                            (date.today() - date(*map(int, birth_date.split('-')))).days,
#                            'A',
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