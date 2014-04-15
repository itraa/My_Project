import flask,flask.views
import settings
import os
import utils
from flask_sqlalchemy import SQLAlchemy
from main import Main
from login import Login
from models import *
from add_breeding_info import *
from add_pups_info import *
from search_breeding_info import *
from search_pups_info import *
from remove_breeding_info import *
import send_reminder

app.secret_key =  settings.secret_key
main_view_func = Main.as_view('main')

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

app.add_url_rule('/add_pups_info/',
                view_func=add_pups_info.as_view('add_pups_info'), 
                methods=['GET','POST'])

app.add_url_rule('/search_breeding_info/',
                view_func=search_breeding_info.as_view('search_breeding_info'), 
                methods=['GET','POST'])

app.add_url_rule('/search_pups_info/',
                view_func=search_pups_info.as_view('search_pups_info'), 
                methods=['GET','POST'])

app.add_url_rule('/remove_breeding_info/',
                view_func=remove_breeding_info.as_view('remove_breeding_info'), 
                methods=['GET','POST'])

@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('404.html'), 404

app.debug = True
use_reloader=False
app.run()