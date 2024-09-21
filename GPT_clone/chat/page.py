import reflex as rx
from GPT_clone import ui



def chat_page():
    
    return ui.base_layout(
         rx.vstack(
            rx.heading("Chat Here", size="9"),            
            spacing="5",
            justify="center",
            min_height="85vh",
        )
    )