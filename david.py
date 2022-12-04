#!/usr/bin/env python3
## The above line is called the shebang, it tells
## terminal that this program should be run in python3 interpreter.
## The python3 interpreter then takes all code that follows and runs
## it. The interpreter will ignore all lines beginning with at least one
## of the "comment character", the pound or hashtag symbol, #

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run(port=5004)