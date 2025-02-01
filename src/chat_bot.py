from typing import Optional
from openai import OpenAI

class ChatBot:
    def __init__(self, api_key: str) -> None:
        self.client: OpenAI = OpenAI(api_key=api_key)

    def chat(self, model: str, user_content: str) -> Optional[str]:
        completion = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": user_content}]
        )
        return completion.choices[0].message if completion.choices else None
