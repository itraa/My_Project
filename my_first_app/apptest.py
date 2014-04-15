import flask, flask.views
import os

app = flask.Flask(__name__)
app.secret_key =  'ba'

class Remote(flask.views.MethodView):
    def get(self):
        return flask.render_template('remote.html')

    def post(self):
        result = eval(flask.request.form['expression'])
        flask.flash(result)
        return flask.redirect(flask.url_for('remote'))
# Routes
app.add_url_rule('/',
                view_func=Remote.as_view('remote'), 
                methods=['GET','POST'])

app.debug = True
app.run()
