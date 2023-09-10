from flask import Blueprint, render_template

# creating a blueprint for the website

auth = Blueprint('auth', __name__)

# Creating route for each page in authentication
@auth.route('/login')
def login():
    return render_template("login.html/")

@auth.route('/logout')
def logout():
    return "<h1>Log Out</h1>"

@auth.route('/sign_up')
def sign_up():
    return render_template("sign_up.html")