from openai import OpenAI

class ImageGenerator:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def generate_image(self, model, prompt, size):
        response = self.client.images.generate(
            model=model,
            prompt=prompt,
            size=size,
            quality="standard",
            n=1
        )
        image_url = response.data[0].url
        return image_url