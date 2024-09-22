import reflex as rx


class ChatState(rx.State):
    did_submit: bool =False
    
    
    @rx.var
    def user_did_submit(self) -> bool: 
        return self.did_submit
    
    def handle_submit(self, form_data:dict):
        # Handle form submission
        print("HERE IS OUR FORM DATA:", form_data)
        self.did_submit = True
    