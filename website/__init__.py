from flask import Flask

def app():
    # initializing flask
    app = Flask(__name__)
    # declaring a secret key for cookies and data purposes
    app.config['SECRET_KEY'] = 'ioengfioun43g#%849uhb24rf2ewdcs!@$#@^'

    # other app configurations, routes, and extensions here

    return app
