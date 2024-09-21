import reflex as rx



from GPT_clone import ui


def about_us_page() -> rx.Component:
    # About Us Page 
    return ui.base_layout(
        rx.vstack(
            rx.heading("Learn about GPT Clone!", size="9"),            
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )



