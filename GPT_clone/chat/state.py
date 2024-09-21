import reflex as rx


class ChatState(rx.State):
    
    def handle_submit(self, form_data:dict):
        # Handle form submission
        print("HERE IS OUR FORM DATA:", form_data)
        
    