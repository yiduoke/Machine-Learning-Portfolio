import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, flash
from random import *
import json, urllib2, sys, os
import sqlite3

UPLOAD_FOLDER = 'scripts-ex1/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def root():
    return render_template("home.html")

@app.route('/linear_regression.html')
def linear_regression():
    return render_template("linear_regression.html")

@app.route('/test', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            # filename = secure_filename(file.filename)
            filename = secure_filename('ex1data3.txt')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/test')
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
    app.debug = True
    app.run()
