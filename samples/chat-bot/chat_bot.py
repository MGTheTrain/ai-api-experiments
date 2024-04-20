import os
import argparse
from openai import OpenAI

class ChatBot:
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def chat(self, system_content, user_content):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content}
            ]
        )
        return completion.choices[0].message

def parse_arguments():
    parser = argparse.ArgumentParser(description="Simple ChatBot")
    parser.add_argument("--model", type=str, default="gpt-3.5-turbo", choices=["gpt-3.5-turbo", "gpt-4-turbo"], help="Model to use")
    parser.add_argument("--system", type=str, default="You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.", help="System content")
    parser.add_argument("--user", type=str, default="Compose a poem that explains the concept of recursion in programming.", help="User content")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        chatbot = ChatBot(api_key, model=args.model)
        response = chatbot.chat(args.system, args.user)
        print(response.content)
    else:
        print("Please provide your OpenAI API key.")
