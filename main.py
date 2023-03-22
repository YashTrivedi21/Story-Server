from typing import Union
import uvicorn
from fastapi import FastAPI
import openai
import settings

app = FastAPI()

openai.api_key = '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'

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/{genre}")
def read_item(genre: str):
    command = "Give me a prompt/idea for writing a short story based on genre: " + genre
    prompt = openai.Completion.create(
        engine="text-davinci-003",
        prompt=command,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        frequency_penalty=0.5
    )

    # Get the first choice (i.e. the generated response) from the response object
    chatbot_prompt = prompt.choices[0].text.strip()
    
    print(chatbot_prompt)

    command_heading = "Give me a good story heading based on prompt: " + chatbot_prompt
    heading = openai.Completion.create(
        engine="text-davinci-003",
        prompt=command_heading,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        frequency_penalty=0.5
    )

    chatbot_heading = heading.choices[0].text.strip()

    print(chatbot_heading)
    return {"prompt": chatbot_prompt, "heading" : chatbot_heading}

uvicorn.run(app, port = 8080, host = "0.0.0.0")