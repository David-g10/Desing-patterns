# GPT conversation bridge.

from typing import Protocol


# La interfaz de "implementación"
class ApiConfig(Protocol):
    def connect():
        pass
    
    def create_thread():
        pass

    def add_thread_message():
        pass

# Clase concreta de implementacion.
class OpenAIConfig(ApiConfig):
    def connect(self):
        print("OpenAI connection.")
    
    def create_thread(self):
        print("OpenAI Thread creation.")

    def add_thread_message(self, message):
        print("OpenAI message added to thread. :", message)
        return self

    def run_thread(self):
        print("thread running")


# Clase concreta de implementacion.
class GeminiGoogle(ApiConfig):
    def connect(self):
        print("Gemini connection.")
    
    def create_thread(self):
        print("Gemini Thread creation.")

    def add_thread_message(self, message):
        print("Gemini message added to thread. :", message)
        return self

    def run_thread(self):
        print("thread running")


# Abstraccion:
class ConversationHandler:
    
    def __init__(self, api_handler: ApiConfig) -> None:
        self.api_handler = api_handler
    
    def connect(self):
        self.api_handler.connect()
    
    def create_thread(self):
        self.api_handler.create_thread()
    
    def send_message(self, message):
        self.api_handler.add_thread_message(message).run_thread()



if __name__=='__main__':

    openai_config = OpenAIConfig()
    chat = ConversationHandler(openai_config)
    chat.send_message("hola")







