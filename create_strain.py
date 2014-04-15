import flask, flask.views
import os
import sys
import utils
from flask_sqlalchemy import SQLAlchemy
from models import *

class create_strain(flask.views.MethodView):
    
        
    @utils.login_required
    def get(self):
        return flask.render_template('create_strain.html')
        
    @utils.login_required
    def post(self):
        input1 = strain_info(flask.request.form['strain_name'],
                           flask.request.form['genetic_background'],
                            flask.request.form['coat_color'],
                            flask.request.form['strain_description'],
                            flask.request.form['strain_source'],
                            flask.request.form['source_description'])

        db.session.add(input1)
        db.session.commit()
        flask.flash("The Strain info has been successfully added")
        return flask.redirect(flask.url_for('create_strain'))        