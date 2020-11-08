"""Import os and dotenv."""
import os
from dotenv import load_dotenv

# Here we set up all our configurations for the app. We are putting it in a
# class so what we can be OOP friendly and break up our code. Additionally,
# we could define different types of configurations that inherit from the
# main Config class. Each child Config class could be for a different stage in
# the process such as: development, testing, production. We won't create
# multiple classes here however, it's good to know what can be done for
# future projects.


class Config:
    """Config class."""

    # We want to start in development mode with debug on so that if we are
    # running the app, it will automatically refresh when we make changes.
    ENV = "development"
    DEBUG = True

    # TODO: create a .env file. In the .env file create a SECRET_KEY and a
    # SQLALCHEMY_DATABASE_URI. We are defining those in the .env so that
    # they are kept private from others.

    # TODO: add SECRET_KEY here using os.getenv method

    # TODO: add SQLALCHEMY_DATABASE_URI here using os.getenv method

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # Here we set our FLASK_ADMIN_SWATCH to "lux". This is a styling template
    # from Bootstrap that will make our admin panel a bit easier to look at
    FLASK_ADMIN_SWATCH = "lux"
    # TODO: go to the_vault/__init__.py
