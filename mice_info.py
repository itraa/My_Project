import flask, flask.views
import os
import sys
import utils
from flask_sqlalchemy import SQLAlchemy
from models import *

class mice_info(flask.views.MethodView):
    
        
    @utils.login_required
    def get(self):
        return flask.render_template('mice_info.html')
        
    @utils.login_required
    def post(self):

        search_dict = {}
        search_list = []
#        item = flask.request.form['bc']
        __table__ = strain_info
        search = __table__.query.order_by(__table__.Strain_id)

#        if len(search) == 0:
#            flask.abort(404)
#        else:
        for result in search:            
            search_dict = dict((col,getattr(result,col)) for col in result.__table__.columns.keys())
            search_list.append(search_dict)
        return flask.render_template('create_mice_list.html', search_list=search_list, search_dict=search_dict)

#        return flask.render_template('mice_info.html',search=search)
