"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Reliable import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/events')
def events():
    """Renders the lockwood page."""
    return render_template(
        'events.html',
        title='Events',
        year=datetime.now().year,
        message='Your events page.'
    )

@app.route('/lockwood')
def lockwood():
    """Renders the lockwood page."""
    return render_template(
        'lockwood.html',
        title='Lockwood',
        year=datetime.now().year,
        message='Your lockwood page.'
    )

@app.route('/reliable')
def reliable():
    """Renders the reliable page."""
    return render_template(
        'reliable.html',
        title='Reliable Street',
        year=datetime.now().year,
        message='Your reliable page.'
    )

@app.route('/thrift')
def thrift():
    """Renders the thrift page."""
    return render_template(
        'thrift.html',
        title='Thrift',
        year=datetime.now().year,
        message='Your thrift description page.'
    )

@app.route('/bikes')
def bikes():
    """Renders the bike page."""
    return render_template(
        'bikes.html',
        title='Bikes',
        year=datetime.now().year,
        message='Your bike description page.'
    )
