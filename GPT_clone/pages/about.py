import reflex as rx



from GPT_clone import ui

class State(rx.State):
    """The app state."""

    ...



def about_us() -> rx.Component:
    # About Us Page 
    return ui.base_layout(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Learn about GPT Clone!", size="9"),            
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )



