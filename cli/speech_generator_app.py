import os
import argparse
from pathlib import Path
from src.speech_generator import TextToSpeechGenerator
import uuid

# Generate a random ID and create the file name
def generate_output_path() -> str:
    random_id = str(uuid.uuid4())  
    file_name = f"{random_id}.mp3"  

    output_dir = "outputs"  
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  

    output_path = os.path.join(output_dir, file_name)
    return output_path

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Text-to-Speech Generator")
    parser.add_argument("--model", type=str, choices=["tts-1", "tts-1-hd"], default="tts-1", help="Model to use (default: tts-1)")
    parser.add_argument("--voice", type=str, choices=["alloy", "echo", "fable", "onyx", "nova", "shimmer"], help="Voice to use (default: alloy)")
    parser.add_argument("--prompt", type=str, required=True, help="Input prompt for generating speech")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        tts_generator = TextToSpeechGenerator(api_key)
        output_path = generate_output_path()
        tts_generator.generate_speech(args.model, args.voice, args.prompt, output_path)
        absolute_output_path = os.path.abspath(output_path)
        print("Speech generated successfully:", absolute_output_path)
    else:
        print("Please provide your OpenAI API key.")
