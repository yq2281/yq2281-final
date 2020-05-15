#******************************************************************************
#Author: Yi Qu
#UNI: yq2281
#Description: This module imports Flask, creates static routes to three pages,
#and starts the server.
#******************************************************************************


#Imports statements.
from flask import Flask, render_template


#Flask app variable.
app = Flask(__name__)


#Static route to main home page.
@app.route("/")
def mainpage():
    return render_template("index.html")


#Static route to classes page.
@app.route("/courses")
def classespage():
    return render_template("courses.html")


#Static route to poetry page.
@app.route("/poetry")
def poetrypage():
    return render_template("poetry.html")


#Starts the server.
if __name__ == "__main__":
    app.run()
    
    