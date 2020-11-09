"""Import libraries."""
from flask import redirect, url_for
from flask_admin import AdminIndexView
from flask_login import current_user


class RestrictedAdminIndexView(AdminIndexView):
    """Admin view custom class."""

    def is_accessible(self):
        """Return True is current user is authenticated."""
        return current_user.is_admin

    # Last time we created the inaccessible_callback function. This function
    # redirects the user if they do not have permission to the admin panel.
    # TODO: Let's change this to redirect the user to the login instead.
    def inaccessible_callback(self, name, **kwargs):
        """Redirect user to login if not authenticated."""
        return redirect(url_for("main.home"))

    # TODO: lastly, uncomment the comments in the_vault/templates/home.html.j2
    # After this try running the app.
