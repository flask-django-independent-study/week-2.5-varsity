"""Import libraries."""
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from the_vault.config import Config

# Here we import RestrictedAdminIndexView. We will go over this later.
# For now just know that it is here
from the_vault.admin import RestrictedAdminIndexView

# Here we create an instantiation from each class of the imported libraries.
# We are not passing in app as an arguement. We will define that later.
db = SQLAlchemy()
# We instantiate admin with a template_mode of bootstrap4
# This allows the admin page be styled by the bootstrap theme that we
# specified in the Config class
admin = Admin(template_mode="bootstrap4")
# Bcrypt is used to hash passwords
bcrypt = Bcrypt()
# TODO: instantiate LoginManager

# TODO: set the login_manager.login_view to "users.login" this tells the
# LoginManager where to redirect the user if they are trying to access a page
# which requires them to be logged in.

# TODO: set the login_manager.session_protection to "strong" you can read more
# about strong mode here:
# https://flask-login.readthedocs.io/en/latest/#session-protection


def create_app(config_class=Config):
    """Create an instance of the vault app."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)

    # TODO: call the init_app method on the login_manager instance and pass in app

    # TODO: call the init_app method on admin and pass in app and
    # index_view=RestrictedAdminIndexView()

    from the_vault.main.routes import main
    from the_vault.users.routes import users

    app.register_blueprint(main)
    app.register_blueprint(users)

    with app.app_context():
        db.create_all()

    return app


# TODO: try running the app and see what happens
# TODO: try going to the "/admin" url and see what happens
# TODO: go to the_vault/models.py
