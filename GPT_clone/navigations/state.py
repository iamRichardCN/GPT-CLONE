import reflex as rx

from . import routes


class NavState(rx.State):
    def to_home(self):
        """
        for on click events
        """
        return rx.redirect(routes.HOME_ROUTE)
    def to_about(self):
        """
        for on click events
        """
        return rx.redirect(routes.ABOUT_US_ROUTE)