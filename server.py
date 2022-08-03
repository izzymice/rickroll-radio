import fastapi, uvicorn, asyncio
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = fastapi.FastAPI(
    title="ash things",
    description="A side where ash keeps his screenshot and links.",
    version="1.0.0"
)

debug = True

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static/html")

some_file_path = "rickroll.mp3"

file = None

async def fake_video_streamer():
    while True:
        with open(some_file_path, "rb") as f: yield f.read()
        await asyncio.sleep(3)

@app.get("/")
def main(request: fastapi.Request):
    return templates.TemplateResponse("home.html", {"request": request})
   # return fastapi.responses.RedirectResponse("/radio.mp3", 302)

@app.get("/radio.mp3")
async def main():
    return fastapi.responses.StreamingResponse(fake_video_streamer(), media_type="audio/mp3")

if __name__ == "__main__":
    config = uvicorn.Config(
        app=app,
        host="127.0.0.1",
        port=80,
        reload=debug
    )
    server = uvicorn.Server(config=config)
    server.run()