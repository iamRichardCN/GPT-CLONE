import reflex as rx
from decouple import config


DATABASE_URL = config("DATABASE_URL", default=None)


config = rx.Config(
    app_name="GPT_clone",
    db_url=DATABASE_URL
)