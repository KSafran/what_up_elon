'''Load Flask App'''
# pylint: disable=invalid-name, wrong-import-position

from flask import Flask
app = Flask(__name__)
from app import routes
