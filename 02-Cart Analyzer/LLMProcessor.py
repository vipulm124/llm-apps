import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from dotenv import load_dotenv
from llmhandlers import LLMPROVIDERS
from llmhandlers import get_llm_provider, get_model
from typing import Optional, List
import json

load_dotenv()


class LLMProcessor:
    def __init__(self, provider: LLMPROVIDERS):
        self.provider = property
        self.model_name = get_model(provider=provider)
        self.llmhandler = get_llm_provider(provider=provider)
        self.conversation_history = []
        self.image_context : Optional[str] = None
    

    def __add_user_chat(self, text:str) -> None:
        conversation = {
            "role": "user",
            "content": text
        }
        self.conversation_history.append(conversation)
    

    def __add_model_response(self, model_response: str) -> None:
        conversation = {
            "role": "system",
            "model": self.model_name,
            "content": model_response
        }
        self.conversation_history.append(conversation)


    def initiate_chat(self, user_input: str, include_context: List = []):
        self.__add_user_chat(user_input)
        # print(f"self.image_context: {self.image_context}")

        model_response= self.llmhandler.start_conversation(user_input, input_context=self.image_context )
        print(f"got response from model: {model_response}")

        self.__add_model_response(model_response)


    def read_screenshots(self, screenshot_paths: list[str]):
        read_screenshot_response = self.llmhandler.read_screenshots(screenshot_paths=screenshot_paths)
        print(f"read_screenshot_response : {read_screenshot_response}")
        if read_screenshot_response is not None:
            self.image_context = read_screenshot_response
            print(f"self.image_context from read_screenshots: {self.image_context}")
            self.__add_model_response(read_screenshot_response)

