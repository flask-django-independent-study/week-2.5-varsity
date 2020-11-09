"""Import libraries."""
from flask import render_template, Blueprint, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user
from the_vault import db
from the_vault.models import User

# TODO: import RegistrationForm, LoginForm, and UpdateAccountForm

users = Blueprint("users", __name__)

# TODO: create a login route with the methods GET and POST.
# TODO: check if the current user is already logged in. If they are, there is
# no point in accessing the login page so we will redirect them to
# "users.account" which is a route we will create.
# TODO: validate the login form, check the password, login the user,
# and redirect them to "users.account"
# TODO: if the form is valid but the check_password returned false, flash
# a message to the user letting them know of the unsuccessful login.
# TODO: if the form is not valid this either means the user enter incorrect
# information or they are going to "/login" as a GET request. Either way,
# return render_template to "login.html.j2" along with the correct form


# TODO: create a register route with the methods GET and POST.
# TODO: check if the current user is already logged in. If they are, there is
# redirect them to "users.account"
# TODO: return the correct template along with the correct form
# TODO: check if the form is valid. If it is, create a new user by passing in
# the form's email data to the User database class. Check if the user is an
# admin, set the users password, add the user to the database, commit the
# database, flash a message saying the account has been created, then
# redirect the user to the login route.


# TODO: create an account route. This routes needs the login_required decorator
# We only want logged in users to access their account.
# IMPORTANT: do not call this decorator by using () after it.
# TODO: This route should have both GET and POST methods. We want to query
# for the current user and return a template along with the user and the
# correct form.
# TODO: make sure the form.email.data = current_user.email this way the form
# prepopulates with the current user's email
# TODO: if the form is validated we want to update the user's email, commit it
# to the database, flash a message, and redirect the user back to
# users.account


# TODO: create a logout route. This route needs the login_required decorator
# TODO: this route function should logout the user and then redirect them to
# main.home


# TODO: go to the_vault/__init__.py
