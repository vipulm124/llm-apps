from .base import LLMBase
from typing import List, Optional
from .constants import PROMPT_PROCESS_SCREENSHOTS, OPENAI_API_KEY, PROMPT_CONVERSATION
from openai import OpenAI
from .utility import get_encoding_for_images, encode_image
from openai.types.chat import ChatCompletionContentPartImageParam


class OpenAILLM(LLMBase):
    def __init__(self, model_name: str):
        self.openai_client = OpenAI(api_key=OPENAI_API_KEY) 
        self.model_name = model_name

    
    def start_conversation(self,  user_input: str, input_context: Optional[str] = None, include_context: bool = True) -> str:
        user_question = PROMPT_CONVERSATION.format(input_context)
        print(f"instructions: {user_question}")
        print(f"input: {user_input}")
        llm_reponse = self.openai_client.responses.create(
            model=self.model_name,
            instructions=str(user_question),
            input=user_input
        )
        return llm_reponse.output_text
        # return None
    

    def read_screenshots(self, screenshot_paths: list[str]) -> Optional[str]:
        # Get the encoded images as ChatCompletionContentPartImageParam objects
        image_inputs = list(get_encoding_for_images(image_paths=screenshot_paths))
        
        print("making call to openai api now")
        # Create the content list with text first, then images
        content = [
            {"type": "text", "text": PROMPT_PROCESS_SCREENSHOTS}
        ] + image_inputs

        completion = self.openai_client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": content
                }
            ],
        )

        content = completion.choices[0].message.content if completion and completion.choices and completion.choices[0].message else None
        if content:
            # Remove any markdown code block formatting dynamically
            import re
            # Remove code blocks with any language identifier (```language or ```)
            content = re.sub(r'^```\w*\n?', '', content.strip())
            content = re.sub(r'\n?```$', '', content.strip())
            content = content.strip()
        return content


