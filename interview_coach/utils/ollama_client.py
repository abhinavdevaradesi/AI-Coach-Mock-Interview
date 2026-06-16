import ollama
from typing import List, Dict

class OllamaClient:
    """Wrapper for Ollama chat interactions."""

    def __init__(self, model: str = "llama3.2"):
        self.model = model

    def chat(self, messages: List[Dict]) -> str:
        """Send messages to Ollama and return the response content."""
        response = ollama.chat(
            model=self.model,
            messages=messages
        )
        return response["message"]["content"]