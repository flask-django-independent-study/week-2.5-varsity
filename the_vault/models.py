"""Import libraries."""
from flask_login import UserMixin, current_user

# Here we import ModelView which serves as the default view in our admin panel
from flask_admin.contrib.sqla import ModelView

# Here we import admin which we will use below.
from the_vault import db, login_manager, bcrypt, admin


@login_manager.user_loader
def load_user(user_id):
    """Get current logged in user."""
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """User database model class."""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=True)
    # Here we create an is_admin property of the user. We set the default to
    # False.
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        """User returns email."""
        if self.is_admin:
            return f"Admin('{self.email}')"
        return f"User('{self.email}')"

    # TODO: create a check_admin method that returns True if the user's email
    # is "admin@admin.com", and returns False otherwise.


# TODO: call the add_view method on admin. add_view takes a view. The view
# will take two arguements, a db class and db.session

# TODO: try running the app and going to "/admin"
# Is this different than before?
# TODO: go to the_vault/admin.py
