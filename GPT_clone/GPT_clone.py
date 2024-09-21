"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from . import chat, pages, navigations






app = rx.App()
app.add_page(pages.home_page, route=navigations.routes.HOME_ROUTE)
app.add_page(pages.about_us_page, route=navigations.routes.ABOUT_US_ROUTE)
app.add_page(chat.chat_page, route=navigations.routes.CHAT_ROUTE)
