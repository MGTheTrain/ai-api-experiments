# python-sample-apps-with-AIaaS-apis

## Table of Contents

+ [Summary](#summary)
+ [Reference](#reference)
+ [Features](#features)
+ [Getting started](#getting-started)

## Summary

Sample apps utilizing AI as a Service (primarily OpenAI and Gemini) Web APIs.

## Reference

- [Get started with the Gemini API](https://ai.google.dev/docs)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference/introduction)
- [OpenAI Models](https://platform.openai.com/docs/models/overview)

### Features

- [x] Chat bot sample app utilizing gpt-3.5-turbo or gpt-4-turbo model
- [ ] Chat bot sample app utilizing Gemini models
- [ ] Image generator sample app utilizing e.g. DALL-E
- [ ] Speech generator sample app

### Getting started

#### Preconditions

- If your IDE supports it, install `Dev Containers extension` or download a [Python 3 Release](https://www.python.org/downloads/)
- Create from the [secrets.template.cfg](./templates/secrets.template.cfg) in the [templates folder](./templates/) a `secrets.cfg` file.
In a Unix-like terminal run the command `source secrets.cfg`.
- Create an `API key` in your OpenAI organization

#### Starting applications

##### Chat bot

```sh
cd samples/chat-bot
pip install -r requirements.txt
```

If **user content does not consist of multiple new lines**:

```sh
python chatbot.py --system <System content here. Can be set to ''> --user <User content here> --model <gpt-3.5-turbo, gpt-4-turbo>

# User content with multiple new lines -> Update the content in the [user-content.txt file](samples/chat-bot/assets/user-content.txt) and run
python chatbot.py --system <System content here. Can be set to ''> --model <gpt-3.5-turbo, gpt-4-turbo>
```

Update the content in the [user-content.txt file](samples/chat-bot/assets/user-content.txt) if **user content consists of multiple new lines**:

```sh
python chatbot.py --system <System content here. Can be set to ''> --model <gpt-3.5-turbo, gpt-4-turbo>

```

**NOTE:** You might need to change your billing plan, if you encounter the error `openai.RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}`

##### Image generator

```sh
cd samples/image-generator
pip install -r requirements.txt
python image_generator.py --model <dall-e-2, dall-e-3> --prompt <user content> --size <size of the image to be generated, e.g. 512x512>
```

##### Speech generator

```sh
cd samples/speech-generator
pip install -r requirements.txt
TBD
```