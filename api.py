from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
import logging

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    logging.info("root api run")
    return {"message": "Hello World"}

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    logging.info("about api run")
    context = {
        "request": request,
        "photo_url": "/static/images/슬기.jpg",
        "name": "김기연",
        "birth": "1998.05.03",
        "university": "명지대학교",
        "major" : "응용소프트웨어",
        "hobby" : "축구, 게임",
        "activities1" : "2024.07 ~ 2025.03 | BoB 13기 보안제품개발",
        "activities2" : "2023.05 ~ 2023.11 | Goorm 1기 정보보호 마스터 클래스",
        "projects1" : "2024.03 | Java Swing 활용 그림판 개발",
        "projects2" : "2023.08 | 네트워크 패킷 분석 시스템 개발"
    }
    return templates.TemplateResponse("about.html", context)

