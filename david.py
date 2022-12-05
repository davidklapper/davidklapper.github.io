#!/usr/bin/env python3
## The above line is called the shebang, it tells
## terminal that this program should be run in python3 interpreter.
## The python3 interpreter then takes all code that follows and runs
## it. The interpreter will ignore all lines beginning with at least one
## of the "comment character", the pound or hashtag symbol, #

from flask import Flask, render_template
import datetime

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route("/")
def root_site():
    mainbody = 'index.txt'
    whoami = 'about.txt'
    art = 'art.txt'
    return render_template('index.html',
                           utc_dt=datetime.datetime.utcnow(),
                           mainbody=mainbody,
                           whoami=whoami,
                           art=art)

@app.route('/about/')
def about():
    include_txt = 'about.txt'
    return render_template('about.html',include_txt=include_txt)


@app.route('/art/')
def art():
    include_txt = 'art.txt'
    return render_template('art.html',include_txt=include_txt)

app.run(port=5004)
