import os, json, urllib2, sys, subprocess
# from subprocess import call
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

UPLOAD_FOLDER = 'scripts-ex1/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def root():
    return render_template("home.html")

@app.route('/linear_regression.html', methods=['GET', 'POST'])
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
            filename = secure_filename('ex1upload.txt')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            myCmd = 'cd ' + UPLOAD_FOLDER + ';'
            myCmd += 'octave ex1.m'
            subprocess.call(myCmd, shell=True) # this blocks

            copyCmd = 'cd ' + UPLOAD_FOLDER + ';'
            copyCmd += 'cp plot.jpg ../static'
            subprocess.call(copyCmd, shell=True)

            return redirect('/linear_regression_results.html')
    return render_template("linear_regression.html")

@app.route('/linear_regression_results.html', methods=['GET', 'POST'])
def linregresults():
    return render_template("linear_regression_results.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
