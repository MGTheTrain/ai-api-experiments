from typing import Optional
from openai import OpenAI

class ImageGenerator:
    def __init__(self, api_key: str) -> None:
        self.client: OpenAI = OpenAI(api_key=api_key)

    def generate_image(self, model: str, prompt: str, size: str) -> Optional[str]:
        response = self.client.images.generate(
            model=model,
            prompt=prompt,
            size=size,
            quality="standard",
            n=1
        )
        return response.data[0].url if response.data else None
