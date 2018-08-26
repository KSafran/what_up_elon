'''Define Routes for Elon WYD Site'''
#pylint: disable=cyclic-import
from flask import render_template
from app import app
from .event_registry import get_elon_headlines

@app.route('/')
def index():
    '''Display Elon News'''
    headlines = get_elon_headlines()
    return render_template('index.html', headlines=headlines)
