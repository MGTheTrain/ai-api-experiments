from typing import Optional
from openai import OpenAI

class ChatBot:
    def __init__(self, api_key: str, model: str = "gpt-4o") -> None:
        self.client: OpenAI = OpenAI(api_key=api_key)
        self.model: str = model

    def chat(self, user_content: str) -> Optional[str]:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": user_content}]
        )
        return completion.choices[0].message if completion.choices else None
