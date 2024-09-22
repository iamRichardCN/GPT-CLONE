#import time
import asyncio
import reflex as rx



class ChatMessage(rx.Base):
    message: str
    is_bot: bool = False
    
    
    

class ChatState(rx.State):
    did_submit: bool =False
    
    
    @rx.var
    def user_did_submit(self) -> bool: 
        return self.did_submit
    
    async def handle_submit(self, form_data:dict):
        # Handle form submission
        print("HERE IS OUR FORM DATA:", form_data)
        user_message=form_data.get('message')
        if  user_message:
            self.did_submit = True
            chat_message= ChatMessage(
                message=user_message,
                is_bot=False
                
                )
            yield
            await asyncio.sleep(2)
            self.did_submit = False
            chat_message= ChatMessage(
                message=user_message,
                is_bot=True
            )
            yield
    