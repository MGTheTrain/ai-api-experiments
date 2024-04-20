import os
import argparse
from pathlib import Path
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

def parse_arguments():
    parser = argparse.ArgumentParser(description="Text-to-Speech Generator")
    parser.add_argument("--model", type=str, choices=["tts-1", "tts-1-hd"], default="tts-1", help="Model to use (default: tts-1)")
    parser.add_argument("--voice", type=str, default="alloy", help="Voice to use (default: alloy)")
    parser.add_argument("--input", type=str, required=True, help="Input text for generating speech")
    parser.add_argument("--output", type=str, default="output/speech.mp3", help="Output file path for the generated speech (default: speech.mp3)")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        tts_generator = TextToSpeechGenerator(api_key)
        output_path = Path(__file__).parent / args.output
        tts_generator.generate_speech(args.model, args.voice, args.input, output_path)
        print("Speech generated successfully:", output_path)
    else:
        print("Please provide your OpenAI API key.")
