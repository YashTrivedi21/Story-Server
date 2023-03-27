from typing import Union
import uvicorn
from fastapi import FastAPI
import openai
import settings
from fastapi import Request, responses
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.responses import HTMLResponse
import repo

app = FastAPI()
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))
templates = Jinja2Templates(directory="templates")

openai.api_key = settings.API_KEY
session = repo.getSession()

def getJsonResponse(genre):
    command = "Give me a prompt/idea for writing a short story based on genre: " + genre + " please keep the prompt succint and do not add any extra rubbish words i.e. directly just give the prompt in 2-3 lines."
    prompt = openai.Completion.create(
        engine="text-davinci-003",
        prompt=command,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        frequency_penalty=0.5
    )
    print(prompt)
    # Get the first choice (i.e. the generated response) from the response object
    chatbot_prompt = prompt.choices[0].text.strip()
    
    # print(chatbot_prompt)

    command_heading = "Give me a good story heading based on prompt: " + chatbot_prompt + " please keep the heading succint and do not add any extra rubbish words i.e. directly just give the heading"
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

    # print(chatbot_heading)

    command_hints = "Give me good 3-4 hints for story based on prompt: " + chatbot_prompt + " please keep the hints succint and do not add any extra rubbish words i.e. directly just give the hints"
    hints = openai.Completion.create(
        engine="text-davinci-003",
        prompt=command_hints,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        frequency_penalty=0.5
    )

    chatbot_hints = hints.choices[0].text.strip()

    return {"prompt": chatbot_prompt, "heading" : chatbot_heading, "hints" : chatbot_hints}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    try:
        rows = repo.print_database(session)
        return templates.TemplateResponse('index.html', {'request': request, 'genres': settings.GENRES, 'rows': rows})
    except Exception as e:
        print(e)


@app.get("/genre")
def read_item(request: Request):
    print(request.query_params['genre'])
    data = getJsonResponse(request.query_params['genre'])
    repo.add_story(session, request.query_params['genre'], data['prompt'], data['heading'])
    rows = repo.print_database(session)
    return templates.TemplateResponse('index.html', {'request': request, 'heading': data['heading'], 'prompt': data['prompt'], 'hints': data['hints'], 'genres': settings.GENRES, 'selected_genre': request.query_params['genre'], 'rows': rows})

@app.get("/getGenre")
def get_genres():
    return settings.GENRES

uvicorn.run(app, port = 8080)