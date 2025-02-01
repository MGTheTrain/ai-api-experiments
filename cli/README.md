# cli

CLI tools enabling image generation, speech generation and chatting functionality

### Getting started

#### Preconditions

- If your IDE supports it, install `Dev Containers extension` or download a [Python >=3.7.1 Release](https://www.python.org/downloads/)
- Install pip dependencies: `cd .. && pip install -r requirements.txt && cd -`
- Create an `API key` in your OpenAI organization
- Export the API key in a terminal process: `export OPENAI_API_KEY="<your OPENAI_API_KEY>"` 

### Getting started

#### Launching applications

---

**Chat bot**

If **user content does not consist of multiple new lines** run:

```sh
python chat-bot.py --system <System content here. Can be set to ''> --user <User content here> --model <gpt-3.5-turbo, gpt-4-turbo>
```

Update the content in the [user-content.txt file](chat-bot/assets/user-content.txt) if **user content consists of multiple new lines** and run:

```sh
python chat-bot.py --system <System content here. Can be set to ''> --model <gpt-3.5-turbo, gpt-4-turbo>

```

**NOTE:** You might need to change your billing plan, if you encounter the error `openai.RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}`

---

**Image generator**

Install pip dependencies and run application:

```sh
python image-generator.py --model <dall-e-2, dall-e-3> --prompt "<user content>" --size <size of the image to be generated, e.g. 1024x1024>
# Checkout link of `Generated image URL` in a browser of choice
```

**NOTE:** ["When using DALL·E 3, images can have a size of 1024x1024, 1024x1792 or 1792x1024 pixels."](https://platform.openai.com/docs/guides/images/usage?context=node)

---

**Speech generator**

Install pip dependencies and run application:

```sh
python speech-generator.py --model tts-1-hd --voice alloy --input "Hello, how are you today?" --output output/hello.mp3
```