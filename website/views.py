from flask import Blueprint, render_template

# creating a blueprint for the website

views = Blueprint('views', __name__)

@views.route('/')
def home_page():
    return render_template("home_page.html")
