from flask import Blueprint

# creating a blueprint for the website

views = Blueprint('views', __name__)

@views.route('/')
def home_page():
    return "<h1>Test<h1>"
