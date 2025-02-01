import os
import argparse
from typing import Optional
from src.chat_bot import ChatBot

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple ChatBot")
    parser.add_argument("--model",  type=str, default="gpt-4o", choices=["gpt-4o", "gpt-4o-mini"], help="Model to use")
    parser.add_argument("--prompt", required=True, type=str, default="Name me the Millennium Prize Problems and provide me an easy explanation in 2 sentences per problem", help="User prompt")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    user_prompt = args.prompt
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        chatbot = ChatBot(api_key)
        response = chatbot.chat(args.model, user_prompt)
        print(response.content)
    else:
        print("Please provide your OpenAI API key.")
