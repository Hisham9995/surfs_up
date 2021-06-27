# Import dependencies 
import datetime as dt
import flask
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, app, jsonify


#  Set up Flask
app = Flask(__name__)
# a new Flask app instance. "Instance" is a general term in programming to refer to a singular version of something.
# ou can use the __name__ variable to determine if your code is being run from the command line or 
# if it has been imported into another piece 
#  Variables with underscores before and after them are called magic methods

# define the starting point also known as the root
#The forward slash is commonly known as the highest level of hierarchy in any computer system.
@app.route('/')
def hello_world():
    return 'Hello world'

