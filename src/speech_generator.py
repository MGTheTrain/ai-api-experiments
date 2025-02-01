from typing import Optional
from openai import OpenAI

class TextToSpeechGenerator:
    def __init__(self, api_key: str) -> None:
        self.client: OpenAI = OpenAI(api_key=api_key)

    def generate_speech(self, model: str, voice: str, input_text: str, output_path: str) -> Optional[bool]:
        response = self.client.audio.speech.create(
            model=model,
            voice=voice,
            input=input_text
        )
        if response:
            response.stream_to_file(output_path)
            return True
        return None
