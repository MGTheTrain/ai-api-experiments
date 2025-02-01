from openai import OpenAI

class TextToSpeechGenerator:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def generate_speech(self, model, voice, input_text, output_path):
        response = self.client.audio.speech.create(
            model=model,
            voice=voice,
            input=input_text
        )
        response.stream_to_file(output_path)