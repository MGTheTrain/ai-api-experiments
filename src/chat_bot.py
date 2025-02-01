from openai import OpenAI

class ChatBot:
    def __init__(self, api_key, model="gpt-4o"):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def chat(self, system_content, user_content):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": user_content}
            ]
        )
        return completion.choices[0].message
