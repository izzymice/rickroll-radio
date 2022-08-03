import fastapi, uvicorn, asyncio
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# some spaces and ussles stuff are to increse size of this file like this bc replit thinks its html without the ussles stuff so ye dont pull request that

app = fastapi.FastAPI(
    title="ash things",
    description="A side where ash keeps his screenshot and links.",
    version="1.0.0"
)

debug = True

app.mount(
    "/static", 
    StaticFiles(
        directory="static"
    ), 
    name="static"
)
templates = Jinja2Templates(
    directory="static/html"
)

file = None

async def fake_video_streamer():
    while True:
        with open("rickroll.mp3", "rb") as f: 
            yield f.read()
        await asyncio.sleep(3)

@app.get("/")
def main(request: fastapi.Request):
    return templates.TemplateResponse(
        "home.html", 
        {"request": request}
    )

@app.get("/docs")
def docs(request: fastapi.Request):
    return fastapi.responses.RedirectResponse("/")

@app.get("/redoc")
def redoc(request: fastapi.Request):
    return fastapi.responses.RedirectResponse("/")

@app.get("/docs/oauth2-redirect")
def oauth2(request: fastapi.Request):
    return fastapi.responses.RedirectResponse("/")

@app.get("/openapi.json")
def openapi(request: fastapi.Request):
    return fastapi.responses.RedirectResponse("/")


@app.get("/radio.mp3")
async def radio():
    return fastapi.responses.StreamingResponse(
        fake_video_streamer(), 
        media_type="audio/mp3"
    )



if __name__ == "__main__":
    config = uvicorn.Config(
        app=app,
        host="127.0.0.1",
        port=80,
        reload=debug
    )

    server = uvicorn.Server(config=config)
    server.run()