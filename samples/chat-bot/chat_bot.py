import os
import argparse
from openai import OpenAI

class ChatBot:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def chat(self, system_content, user_content):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content}
            ]
        )
        return completion.choices[0].message

def parse_arguments():
    parser = argparse.ArgumentParser(description="Simple ChatBot")
    parser.add_argument("--system", type=str, default="You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.", help="System content")
    parser.add_argument("--user", type=str, default="Compose a poem that explains the concept of recursion in programming.", help="User content")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        chatbot = ChatBot(api_key)
        response = chatbot.chat(args.system, args.user)
        print(response.content)
    else:
        print("Please provide your OpenAI API key.")