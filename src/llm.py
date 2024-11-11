from abc import ABC, abstractmethod

import requests
from fastapi import HTTPException


class LLMClient(ABC):
    @abstractmethod
    def generate_answer(self, prompt: str, model: str, **kwargs): ...


class OllamaCLient(LLMClient):
    def __init__(self, base_url: str = "http://localhost:11434") -> None:
        self.base_url = base_url
        self.api_endpoint = f"{base_url}/api/generate"

    def generate_answer(self, prompt: str, model: str = "llama3.1:8b", **kwargs):
        try:
            payload = {
                "model": model,
                "prompt": prompt,
                "stream": False,
                "format": "json",
                "options": {"temperature": 0.5},
            }

            response = requests.post(self.api_endpoint, json=payload)
            response.raise_for_status()

            result = response.json()
            return result["response"]
        except requests.exceptions.RequestException as e:
            raise HTTPException(
                status_code=500, detail=f"Error communicating with Ollama: {str(e)}"
            )
