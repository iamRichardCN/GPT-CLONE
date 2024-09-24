#import time
from typing import List
import reflex as rx

from . import ai


class ChatMessage(rx.Base):
    message: str
    is_bot: bool = False
    
    
    

class ChatState(rx.State):
    did_submit: bool =False
    messages: list[ChatMessage]= []
    
    
    @rx.var
    def user_did_submit(self) -> bool: 
        return self.did_submit
    
    def append_message(self, message, is_bot:bool=False):
        self.messages.append(
            ChatMessage(
                message=message,
                 is_bot=is_bot
            )
        )        
    
    
    def get_gpt_message(self):
        gpt_messages = [
            {
               "role": "system",
               "content" : "you are an expert in creating recipes like an elite chef. Respond in markdown"
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
        print("HERE IS OUR FORM DATA:", form_data)
        user_message=form_data.get('message')
        if  user_message:
            self.did_submit = True
            self.append_message(user_message, is_bot=False)
            yield
            gpt_messages=self.get_gpt_message()
            print(gpt_messages)
            bot_response=ai.get_llm_response(gpt_messages)
            #await asyncio.sleep(2)
            self.did_submit = False
            self.append_message(bot_response, is_bot=True)
            yield
    