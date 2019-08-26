import os, json, urllib2, sys, subprocess
# from subprocess import call
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

UPLOAD_FOLDER_EX1 = 'scripts-ex1/'

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_EX1

@app.route('/')
def root():
    return render_template("home.html")


###########################Linear Regression##############################
@app.route('/linear_regression.html', methods=['GET', 'POST'])
def linear_regression():
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_EX1
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

            myCmd = 'cd ' + UPLOAD_FOLDER_EX1 + ';'
            myCmd += 'octave ex1.m'
            subprocess.call(myCmd, shell=True) # this blocks

            copyCmd = 'cd ' + UPLOAD_FOLDER_EX1 + ';'
            copyCmd += 'cp plot_ex1.jpg ../static'
            subprocess.call(copyCmd, shell=True)

            return redirect('/linear_regression_results.html')
    return render_template("linear_regression.html")

@app.route('/linear_regression_results.html', methods=['GET', 'POST'])
def lin_reg_results():
    return render_template("linear_regression_results.html")

##########################Logistic Regression##############################
UPLOAD_FOLDER_EX2 = 'scripts-ex2/'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_EX2

@app.route('/logistic_regression.html', methods=['GET', 'POST'])
def logistic_regression():
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_EX2
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
            filename = secure_filename('ex2upload.txt')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            myCmd = 'cd ' + UPLOAD_FOLDER_EX2 + ';'
            myCmd += 'octave ex2.m'
            subprocess.call(myCmd, shell=True) # this blocks

            copyCmd = 'cd ' + UPLOAD_FOLDER_EX2 + ';'
            copyCmd += 'cp plot_ex2.jpg ../static'
            subprocess.call(copyCmd, shell=True)

            return redirect('/logistic_regression_results.html')
    return render_template("logistic_regression.html")

@app.route('/logistic_regression_results.html', methods=['GET', 'POST'])
def log_reg_results():
    return render_template("logistic_regression_results.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
