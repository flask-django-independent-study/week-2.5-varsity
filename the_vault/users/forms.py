"""Import libraries."""
# Here we import FlaskForm. This will serve as a base for our forms to build
# off of. In this file we will create a RegistrationForm, LoginForm, and
# UpdateAccountForm
from flask_wtf import FlaskForm
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    ValidationError,
    EqualTo,
)
from wtforms.fields import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
)
from the_vault.models import User

# TODO: create a RegistrationForm class that inherits from FlaskForm.
# It should have email, password, confirm_password, and a Register button.
# TODO: create a validate_email method that checks if a user with the email
# already exists. If a user already exists raise a ValidationError

# TODO: create a LoginForm class that inherits from FlaskForm.
# It should have an email, password, and Login button.

# TODO: create an UpdateAccountForm class that inherits from FlaskForm.
# It should have an email and an Update button.
# TODO: create a validate_email method that checks if a user with the email
# already exists. If a user already exists raise a ValidationError

# TODO: go to the_vault/users/routes.py
