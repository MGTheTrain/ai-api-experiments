# python-sample-apps-with-AIaaS-apis

## Table of Contents

+ [Summary](#summary)
+ [Reference](#reference)
+ [Features](#features)
+ [Getting started](#getting-started)

## Summary

Sample apps utilizing AI as a Service (primarily OpenAI) Web APIs.

## Reference

- [OpenAI API Reference](https://platform.openai.com/docs/api-reference/introduction)
- [OpenAI Models](https://platform.openai.com/docs/models/overview)
- [Get started with the Gemini API](https://ai.google.dev/docs)

### Features

- [x] Chat bot sample app utilizing gpt-3.5-turbo or gpt-4-turbo model
- [x] Image generator sample app utilizing dall-e-2 or dall-e-3 model
- [x] Speech generator sample app utilizing tts-1 or tts-1-hd model

### Getting started

#### Preconditions

- If your IDE supports it, install `Dev Containers extension` or download a [Python >=3.7.1 Release](https://www.python.org/downloads/)
- Create from the [secrets.template.cfg](./templates/secrets.template.cfg) in the [templates folder](./templates/) a `secrets.cfg` file.
In a Unix-like terminal run the command `source secrets.cfg`.
- Create an `API key` in your OpenAI organization

#### Starting applications

---

**Chat bot**

Install pip dependencies:

```sh
cd samples/chat-bot
pip install -r requirements.txt
```

If **user content does not consist of multiple new lines**, run:

```sh
python chatbot.py --system <System content here. Can be set to ''> --user <User content here> --model <gpt-3.5-turbo, gpt-4-turbo>

# User content with multiple new lines -> Update the content in the [user-content.txt file](samples/chat-bot/assets/user-content.txt) and run
python chatbot.py --system <System content here. Can be set to ''> --model <gpt-3.5-turbo, gpt-4-turbo>
```

Update the content in the [user-content.txt file](samples/chat-bot/assets/user-content.txt) if **user content consists of multiple new lines**, run:

```sh
python chatbot.py --system <System content here. Can be set to ''> --model <gpt-3.5-turbo, gpt-4-turbo>

```

**NOTE:** You might need to change your billing plan, if you encounter the error `openai.RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}`

---

**Image generator**

Install pip dependencies and run application:

```sh
cd samples/image-generator
pip install -r requirements.txt
python image_generator.py --model <dall-e-2, dall-e-3> --prompt "<user content>" --size <size of the image to be generated, e.g. 1024x1024>
# Checkout link of `Generated image URL` in a browser of choice
```

**NOTE:** ["When using DALL·E 3, images can have a size of 1024x1024, 1024x1792 or 1792x1024 pixels."](https://platform.openai.com/docs/guides/images/usage?context=node)

---

**Speech generator**

```sh
cd samples/speech-generator
pip install -r requirements.txt
python speech_generator.py --model tts-1-hd --voice alloy --input "Hello, how are you today?" --output output/hello.mp3
```