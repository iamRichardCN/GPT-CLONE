#import time
from typing import List
import reflex as rx
from GPT_clone.models import chat
from . import ai2


class ChatMessage(rx.Base):
    message: str
    is_bot: bool = False
    
    
    

class ChatState(rx.State):
    did_submit: bool =False
    messages: list[ChatMessage]= []
    
    
    @rx.var
    def user_did_submit(self) -> bool: 
        return self.did_submit
    
    
    def on_load(self):
        with rx.session as session:
           results = session.exec(
                chat.select()
            ).all()
           print(results)
           
            
        
    
    def append_message(self, message, is_bot:bool=False):
        self.messages.append(
            ChatMessage(
                message=message,
                 is_bot=is_bot
            )
        )        
    
#actual working chatgpt model
    def get_gpt_message(self):
        gpt_messages = [
            {
               "role": "system",
               "content" : "Respond in markdown and make sure you are brief but please dont add any answer to what was never asked, be concise to maximise you 200 tokens"
            }
        ]
        for chat_message in self.messages:
            role='user'
            if chat_message.is_bot:
                role="system"
            gpt_messages.append({
                "role": role,
                "content": chat_message.message
            })   
        return gpt_messages
    
    async def handle_submit(self, form_data:dict):
        # Handle form submission
        #print("HERE IS OUR FORM DATA:", form_data)
        user_message=form_data.get('message')
        if  user_message:
            self.did_submit = True
            self.append_message(user_message, is_bot=False)
            yield
            gpt_messages=self.get_gpt_message()
            bot_response=ai2.get_llm_response(gpt_messages)
            #await asyncio.sleep(2)
            self.did_submit = False
            self.append_message(bot_response, is_bot=True)
            yield
