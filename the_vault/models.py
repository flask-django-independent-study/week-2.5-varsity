"""Import libraries."""
from flask_login import UserMixin, current_user
from flask_admin.contrib.sqla import ModelView
from the_vault import db, login_manager, bcrypt, admin

# This load_user function gets called behind the scenes everytime the
# login_manager needs to check the current_user. The user that gets returned
#  in the query is then assigned as the current_user
@login_manager.user_loader
def load_user(user_id):
    """Get current logged in user."""
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """User database model class."""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        """User returns email."""
        if self.is_admin:
            return f"Admin('{self.email}')"
        return f"User('{self.email}')"

    def check_admin(self):
        """Check if user is authorized to be an admin."""
        if self.email == "admin@admin.com":
            self.is_admin = True

    # TODO: create a set_password method that takes in self and password as
    # arguments. Call bcrypt.generate_password_hash and pass in the password.
    # Then set this as the user's password
    # HINT: bcrypt encrypts the password as a byte, which is a data type
    # that contains binary data. The generated password has will need to be
    # decoded to utf-8

    # TODO: create a check_password method that takes in self and password as
    # arguments. Call bcrypt.check_password_hash and pass in the user's
    # password along with the password to be checked. Return the result.
    # check_password_hash returns True is the passwords match and False
    # otherwise


admin.add_view(ModelView(User, db.session))

# TODO: go to the_vault/users/forms.py
