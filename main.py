from typing import Union

from fastapi import FastAPI
import openai
import settings

app = FastAPI()

openai.api_key = settings.API_KEY

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/prompt/{prompt}")
def read_item(prompt: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        frequency_penalty=0.5
    )

    # Get the first choice (i.e. the generated response) from the response object
    chatbot_response = response.choices[0].text.strip()
    
    print(chatbot_response)
    return {"prompt": chatbot_response}