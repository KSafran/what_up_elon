from flask import render_template
from app import app
from .event_registry import get_elon_headlines

@app.route('/')
def index():
    headlines = get_elon_headlines()
    return render_template('index.html', headlines = headlines)

