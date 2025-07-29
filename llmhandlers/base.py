# from constants import LLMPROVIDERS
from abc import ABC, abstractmethod
from typing import List, Optional

class LLMBase(ABC):
    @abstractmethod
    def start_conversation(self, user_input: str, input_context: Optional[str] = None, include_context: bool = True) -> str:
        """
        start conversation with LLM
        """
    
    @abstractmethod
    def read_screenshots(self, screenshot_paths: list[str]) -> Optional[str]:
        """
        read screenshots and process information
        """