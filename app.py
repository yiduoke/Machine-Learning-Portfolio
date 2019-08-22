from flask import Flask, render_template, request, redirect, url_for, flash
from random import *
import json, urllib2, sys, os
import sqlite3

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("home.html")

@app.route('/linear_regression.html')
def linear_regression():
    return render_template("linear_regression.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
