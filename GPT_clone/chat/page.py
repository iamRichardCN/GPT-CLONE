import reflex as rx
from GPT_clone import ui
from .form import chat_form


def chat_page():
    
    return ui.base_layout(
         rx.vstack(
            rx.heading("Chat Here", size="9"), 
            chat_form(),           
            spacing="5",
            justify="center",
            min_height="85vh",
        )
    )