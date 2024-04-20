import os
import argparse
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

def parse_arguments():
    parser = argparse.ArgumentParser(description="Image Generator")
    parser.add_argument("--model", type=str, choices=["dall-e-2", "dall-e-3"], default="dall-e-3", help="Model to use (default: dall-e-3)")
    parser.add_argument("--prompt", type=str, required=True, default="A colorful butterfly", help="Prompt for generating the image")
    parser.add_argument("--size", type=str, default="1024x1024", help="Size of the generated image (default: 1024x1024)")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        image_generator = ImageGenerator(api_key)
        image_url = image_generator.generate_image(args.model, args.prompt, args.size)
        print("Generated image URL:", image_url)
    else:
        print("Please provide your OpenAI API key.")
