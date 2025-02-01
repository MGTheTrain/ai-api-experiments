import os
import argparse
from pathlib import Path
from src.speech_generator import TextToSpeechGenerator

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Text-to-Speech Generator")
    parser.add_argument("--model", type=str, choices=["tts-1", "tts-1-hd"], default="tts-1", help="Model to use (default: tts-1)")
    parser.add_argument("--voice", type=str, choices=["alloy", "echo", "fable", "onyx", "nova", "shimmer"], help="Voice to use (default: alloy)")
    parser.add_argument("--input", type=str, required=True, help="Input text for generating speech")
    parser.add_argument("--output", type=str, default="outputs/speech.mp3", help=f"Output file path for the generated speech (default: speech.mp3).  \n"
                                                                                f"Check list of supported output formats: https://platform.openai.com/docs/guides/text-to-speech")
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
