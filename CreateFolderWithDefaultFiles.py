"""
Script to create folder in specified location and copy default files into it
If folder exists, create the default files

"""

from flask import Flask

app=Flask(__name__)

@app.route("/")
def Hello():
    return "Hello Wo"


