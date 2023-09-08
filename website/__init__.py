from flask import Flask

def app():
    # initializing flask
    app = Flask(__name__)
    # declaring a secret key for cookies and data purposes
    app.config['SECRET_KEY'] = 'ioengfioun43g#%849uhb24rf2ewdcs!@$#@^'

    # routes
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_perfix='/')
    app.register_blueprint(auth, url_perfix='/')

    return app
