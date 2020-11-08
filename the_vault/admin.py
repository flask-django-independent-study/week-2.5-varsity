"""Import libraries."""
from flask import redirect, url_for

# We import AdminIndexView. This is the view that allows us to see the
# admin panel for our site
from flask_admin import AdminIndexView
from flask_login import current_user

# We pass in AdminIndexView view to our new class RestrictedAdminIndexView.
# You saw that we imported this class in the __init__.py file.
# This class will inherit from AdminIndexView. We will override two of its
# methods in order to restrict access to the admin panel.
class RestrictedAdminIndexView(AdminIndexView):
    """Admin view custom class."""

    # TODO: remove pass. This is just here as a placeholder.

    # TODO: create an is_accessible method. This will override the default
    # method. This method will allow access to the admin panel if it
    # returns True.
    # TODO: Return True is the current user is an admin and False if the
    # user is not an admin

    # TODO: create an inaccessible_callback method. This will override the
    # default method. It should take in self (like all methods), name, and
    # **kwargs as parameters. This method will tell the app what to do if
    # a user tries to access the admin page but does not have access
    # TODO: redirect the user to the home route if they do not have access


# TODO: try running the app and going to "/admin"
# What happened?

# NOW THE ADMIN PART IS COMPLETED! GO TO THE REPO "week-2.5-varsity" TO
# COMPLETE TO LOGIN PART OF THE ASSIGNMENT
# https://github.com/flask-django-independent-study/week-2.5-varsity
