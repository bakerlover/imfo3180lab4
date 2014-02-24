"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask
from flask import jsonify
from flask import render_template
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/cat')
def cat(name=None):
  """ Return me template at application /me URL."""
  return render_template('cat.html', name=name)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'



@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404

@app.route('/madlibs')
def madlibs(name=None):
  """ Return me template at application /madlibs URL."""
  return render_template('madlibs.html', name=name)

@app.route('/cal')
def cal(name=None):
  """ Return me template at application /me URL."""
  return render_template('cal.html', name=name)