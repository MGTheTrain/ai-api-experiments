# ai-api-companions

## Table of Contents

+ [Summary](#summary)
+ [Reference](#reference)
+ [Features](#features)
+ [Getting started](#getting-started)

## Summary

Applications providing a user-friendly interface to interact with OpenAI's AIaaS web-backends

## Reference

- [OpenAI API Reference](https://platform.openai.com/docs/api-reference/introduction)
- [OpenAI Models](https://platform.openai.com/docs/models/overview)
- [Get started with the Gemini API](https://ai.google.dev/docs)

### Features

- [x] Chat bot CLI Tool utilizing gpt-3.5-turbo or gpt-4-turbo model
- [x] Image generator CLI Tool utilizing dall-e-2 or dall-e-3 model
- [x] Speech generator CLI Tool utilizing tts-1 or tts-1-hd model
- [ ] Desktop application designed to provide a user-friendly interface for interacting with OpenAI’s AIaaS web-backends enabling image generation, speech generation and chatting functionality

### Getting started

#### Preconditions

- If your IDE supports it, install `Dev Containers extension` or download a [Python >=3.7.1 Release](https://www.python.org/downloads/)
- Install pip dependencies: `pip install -r requirements.txt`
- Create an `API key` in your OpenAI organization
- Export the API key in a terminal process: `export OPENAI_API_KEY="<your OPENAI_API_KEY>"` 

#### CLI tools

Check out the [cli README.md](./cli/README.md) for more information on the sample CLI tools

#### Launching the Desktop app

Run:

```sh
cd desktop-ui
python companion.py
```