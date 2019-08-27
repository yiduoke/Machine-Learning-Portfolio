import os, json, urllib2, sys, subprocess
# from subprocess import call
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

UPLOAD_FOLDER_EX1 = 'scripts-ex1/'

app = Flask(__name__)

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

##########################Neural Network##############################
UPLOAD_FOLDER_EX3 = 'scripts-ex3/'

@app.route('/neural_network.html', methods=['GET', 'POST'])
def neural_network():
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_EX3
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
            filename = secure_filename('ex3upload.png')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            myCmd = 'cd ' + UPLOAD_FOLDER_EX3 + ';'
            myCmd += 'octave ex3_nn.m'
            subprocess.call(myCmd, shell=True) # this blocks

            return redirect('/neural_network_results.html')
    return render_template("neural_network.html")

@app.route('/neural_network_results.html', methods=['GET', 'POST'])
def neu_net_results():
    f = open("scripts-ex3/output.txt", "r")
    output = f.read()
    f.close()

    if output == "10":
        output = 0
    return render_template("neural_network_results.html", number = output)


##########################Support Vector Machine##############################
UPLOAD_FOLDER_EX6 = 'scripts-ex6/'

@app.route('/svm.html', methods=['GET', 'POST'])
def svm():
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_EX6
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
            filename = secure_filename('ex6upload.txt')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            myCmd = 'cd ' + UPLOAD_FOLDER_EX6 + ';'
            myCmd += 'octave ex6_spam.m'
            subprocess.call(myCmd, shell=True) # this blocks

            return redirect('/svm_results.html')
    return render_template("svm.html")

@app.route('/svm_results.html', methods=['GET', 'POST'])
def svm_results():
    f = open("scripts-ex6/output.txt", "r")
    content = f.read()
    f.close()

    output = "It's not spam!"
    if content == "1":
        output = "It's spam!"
    return render_template("svm_results.html", result = output)


if __name__ == "__main__":
    app.debug = True
    app.run()
