import fastapi
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from tools import thumb,data,getvideo



app = fastapi.FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

thumb.update()
data.update()

@app.get("/")
async def home(request: Request):
    videos = getvideo.format()
    return templates.TemplateResponse(
        request=request, name="home.html",context={"content":videos,"length":len(videos)})

@app.get("/video/{i}")
async def video_page(request: Request,i:str):
    return templates.TemplateResponse(
        request=request, name="video.html",context={"i":i,"title":data.get(i)["name"]})


@app.get("/bootstrap.js")
async def bsj():
    return FileResponse("./bootstrap.js")

@app.get("/bootstrap.css")
async def bsc():
    return FileResponse("./bootstrap.css")

@app.get("/thumb/{i}")
async def getThumb(i):
    return FileResponse(f"thumbnail/{i}.jpg")

@app.get("/getvideo/{i}")
async def getVideo(i):
    return FileResponse(f"video/{i}.mp4")


class NameIdPair(BaseModel):
    id:str
    name:str

@app.post("/updateName/")
async def updateName(dat:NameIdPair):
    return data.rename(dat.id,dat.name)
    
