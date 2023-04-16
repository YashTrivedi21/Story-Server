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

COUNT = 0

def getJsonResponse(genre):
    
    global COUNT

    print("getJsonResponse called" + str(COUNT))

    COUNT+=1

    # command = "Give me an idea for a 15-minute creative writing exercise. Keep the prompt inspiring like a cliffhanger. Write in German (de-ch). Below the idea, add Ideen fürs Schreiben:  followed by a few hints that guide the writer for completing the assignment. Here are some examples: (Auf der Suchen nach dem heikräftigen Pilz Martin und Julia suchen nach einer geheimnisvollen Siedlung mitten im undurchdringlichen Dschungel des Amazonasgebiets. Dort soll ein seltener, türkis-glänzender Pilz wachsen, der fast alle Krankheiten heilen kann. Ein Trupp bewaffneter Söldner verfolgt sie, um ihnen den Pilz abzujagen und das grosse Geld zu machen. Ideen fürs Schreiben: Warum wollen Martin und Julia den Pilz finden? Wollen Sie einem Angehörigen helfen? Eine Stiftung gründen? Was sonst? Wie sieht die Landschaft im Amazonas aus? Wie bewegen sich die beiden Protagonisten und ihre Verfolger fort? Mit Booten? Mit Jeeps? Mit Flugzeugen? Wem begegnen sie unterwegs, der bei der Suche helfen kann?) (Die schwarze Limousine Als Franz von der Arbeit nach Hause kommt, parkt eine schwarze Limousine in der Einfahrt zu seiner Villa. Alle Lichter im Haus sind hell erleuchtet. Die Haustür steht weit offen, aber es ist kein Geräusch zu hören. Ideen fürs Schreiben: Welche Hoffnungen oder Befürchtungen hat Franz, als er die dunkle Limousine sieht? Was macht Franz beruflich? Besteht ein Zusammenhang zwischen seiner Arbeit und den Ereignissen in seinem Haus? Wie genau sieht das Haus aus? In welcher Umgebung steht es? Was entdeckt Franz, als er das Hause betritt? Wer lebt sonst noch in dem Haus? Seine Ehefrau und Kinder? Oder sein scwuler Partner? Oder seine Mutter mit ihren 12 Katzen?) (Eine Jugendliebe in Paris Gabi schaut aus dem Fenster eines kleinen Pariser Cafés und beobachtet, wie sich die Welt in den Regenpfützen spiegelt. Dann tritt ein Mann in das Café, stellt seinen Regenschirm ab und hängt seinen Mantel an die Garderobe. Gabi traut ihren Augen nicht, als Sie ihre verschollene Jugendliebe erkennt. Ideen fürs Schreiben: Woran erkennt Gabi, dass der Mann ihre Jugendliebe ist? Warum haben die beiden sich aus den Augen verloren? Was ist ihre aktuelle Lebenssituation? Sind beide frei, sich aufeinander einzulassen? Gabi fällt es sicher nicht ganz leicht, den Mann anzusprechen. Beschreibe ihren inneren Zwiespalt.). Also use the genre as: " + genre
    # prompt = openai.Completion.create(
    #     engine="text-davinci-003",
    #     prompt=command,
    #     max_tokens=240,
    #     n=1,
    #     stop=None,
    #     temperature=0.7,
    #     frequency_penalty=0.7,  
    # )
    # # Get the first choice (i.e. the generated response) from the response object
    # chatbot_prompt = prompt.choices[0].text.strip()
    
    
    # command_heading = "Give me a very short story heading based on prompt: " + chatbot_prompt + ". Do not add introductry or closing remarks. Just give the heading. Write in German (de-ch)."
    # heading = openai.Completion.create(
    #     engine="text-davinci-003",
    #     prompt=command_heading,
    #     max_tokens=40,
    #     n=1,
    #     stop=None,
    #     temperature=0.3,
    #     frequency_penalty=0.7
    # )

    # chatbot_heading = heading.choices[0].text.strip()

    
    # command_hints = "Give me 3-4 elaborate hints for a writing assignment based on prompt: " + chatbot_prompt + ". The hints should inspire thinking about the backstory, about the surroundings, the character traits of the characters involved and about the next things that could happen next. Write in hypothetical style like 'Imagine that ...' or 'Consider ...' or 'How would the story contunue ...' or 'Think about ...' or 'What if ...'. Do not add introductry or closing remarks. Just give the hints.Write in German (de-ch). Check for German grammar errors."
    # hints = openai.Completion.create(
    #     engine="text-davinci-003",
    #     prompt=command_hints,
    #     max_tokens=400,
    #     n=1,
    #     stop=None,
    #     temperature=0.7,
    #     frequency_penalty=0.7
    # )

    # chatbot_hints = hints.choices[0].text.strip()

    # return {"prompt": chatbot_prompt, "heading" : chatbot_heading, "hints" : chatbot_hints}

    # command = "Give me an idea for a 15-minute creative writing exercise. Keep the prompt inspiring like a cliffhanger. Write in German (de-ch). Below the idea, add Ideen fürs Schreiben: followed by a few hints that guide the writer for completing the assignment. Use HTML for your repsonse. Here are some examples: (<h2>Auf der Suche nach dem heikräftigen Pilz</h2><p>Martin und Julia suchen nach einer geheimnisvollen Siedlung mitten im undurchdringlichen Dschungel des Amazonasgebiets. Dort soll ein seltener, türkis-glänzender Pilz wachsen, der fast alle Krankheiten heilen kann. Ihre Expedition entwickelt sich zu einem lebensgefährlichen Abenteuer, denn ein Trupp bewaffneter Söldner verfolgt sie, um ihnen den Pilz abzujagen und das grosse Geld zu machen.</p><h3>Ideen fürs Schreiben: </h3><ul><li>Warum wollen Martin und Julia den Pilz finden? Wollen Sie einem Angehörigen helfen? Eine Stiftung gründen? Was sonst?</li><li>Wie sieht die Landschaft im Amazonas aus?</li><li>Wie bewegen sich die beiden Protagonisten und ihre Verfolger fort? Mit Booten? Mit Jeeps? Mit Flugzeugen?</li><li>Wem begegnen sie unterwegs, der bei der Suche helfen kann?</li></ul>) (<h2>Die schwarze Limousine</h2><p>Als Franz von der Arbeit nach Hause kommt, parkt eine schwarze Limousine in der Einfahrt zu seiner Villa. Alle Lichter im Haus sind hell erleuchtet. Die Haustür steht weit offen, aber es ist kein Geräusch zu hören. <h3>Ideen fürs Schreiben:</h3><ul><li>Welche Hoffnungen oder Befürchtungen hat Franz, als er die dunkle Limousine sieht?</li><li>Was macht Franz beruflich?-</li><li>Besteht ein Zusammenhang zwischen seiner Arbeit und den Ereignissen in seinem Haus?/li><li>Wie genau sieht das Haus aus? In welcher Umgebung steht es?</li><li>Was entdeckt Franz, als er das Hause betritt?</li><li>Wer lebt sonst noch in dem Haus? Seine Ehefrau und Kinder? Oder sein schwuler Partner? Oder seine Mutter mit ihren 12 Katzen?</li></ul>) (<h2>Eine Jugendliebe in Paris</h2><p>Gabi schaut aus dem Fenster eines kleinen Pariser Cafés und beobachtet, wie sich die Welt in den Regenpfützen spiegelt. Dann tritt ein Mann in das Café, stellt seinen Regenschirm ab und hängt seinen Mantel an die Garderobe. Gabi traut ihren Augen nicht, als Sie ihre verschollene Jugendliebe erkennt.</p><h3>Ideen fürs Schreiben:</h3><ul><li>Woran erkennt Gabi, dass der Mann ihre Jugendliebe ist?</li><li>Warum haben die beiden sich aus den Augen verloren?</li><li>Was ist ihre aktuelle Lebenssituation? Sind beide frei, sich aufeinander einzulassen? Was hindert sie?</li><li>Gabi fällt es sicher nicht ganz leicht, den Mann anzusprechen. Beschreibe ihren inneren Zwiespalt.</li></ul>. Also use the genre as: " + genre
    command = "Give me a short prompt to write a story in German (de-ch). where heading should be in <h2> tag, main storyline should be in <p> tag and hints should be in <li> tag. Return all this in html format and use the genre as: " + genre
    ans = openai.Completion.create(
        engine="text-davinci-003",
        prompt=command,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.7,
        frequency_penalty=0.7
    )

    print(ans.choices[0].text.strip())
    return ans.choices[0].text.strip()

    

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # return templates.TemplateResponse('index.html', {'request': request})
    try:
        return templates.TemplateResponse('index.html', {'request': request, 'genres': settings.GENRES, 'genre_inc_all': ["All Genres"] + settings.GENRES})
    except Exception as e:
        print(e)


@app.get("/genre")
def read_item(request: Request):
    print(request.query_params['genre'])
    data = getJsonResponse(request.query_params['genre'])
    # print(data)
    repo.add_story(session, request.query_params['genre'], data)
    return templates.TemplateResponse('index.html', {'request': request, 'genres': settings.GENRES, 'selected_genre': request.query_params['genre'], 'genre_inc_all': ["All Genres"] + settings.GENRES, 'response': data})

@app.get("/getGenre")
def get_genres():
    return settings.GENRES

@app.get("/getStories/{genre}")
def get_stories(genre: str):
    return repo.get_stories(session, genre)
    
uvicorn.run(app, port = 8080)
