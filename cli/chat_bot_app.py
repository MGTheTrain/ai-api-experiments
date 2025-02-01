import os
import argparse
from src.chat_bot import ChatBot

def parse_arguments():
    parser = argparse.ArgumentParser(description="Simple ChatBot")
    parser.add_argument("--model", type=str, default="gpt-4o", choices=["gpt-4o", "gpt-4o-mini", "o1", "o3-mini"], help="Model to use")
    parser.add_argument("--prompt", type=str, default="Name me the Millennium Prize Problems and provide me an easy explanation in 2 sentences per problem", help="User prompt")
    parser.add_argument("--file", type=str, default="inputs/user-content.txt", help="Path to a file containing user content in case message contains to many newlines")
    return parser.parse_args()

def load_user_prompt(file_path):
    if not file_path:
        return None
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("User content file not found.")
        return None

if __name__ == "__main__":
    args = parse_arguments()
    user_prompt = args.prompt
    if user_prompt is None:
        user_file='inputs/user-content.txt'
        user_prompt = load_user_prompt(args.file)
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        chatbot = ChatBot(api_key, model=args.model)
        response = chatbot.chat(args.system, user_prompt)
        print(response.content)
    else:
        print("Please provide your OpenAI API key.")
