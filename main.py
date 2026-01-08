from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
import database

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Initialize DB (create data folder)
database.init_db()

@app.get("/")
async def root(request: Request):
    config = database.get_config()
    if not config:
        return templates.TemplateResponse("setup.html", {"request": request})
    
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "username": config.get("username", "User")
    })

@app.post("/setup")
async def setup(request: Request, username: str = Form(...)):
    database.create_config(username)
    return RedirectResponse(url="/", status_code=303)

# Hack to support 'uvicorn main:app.py' (uvicorn treats dots as attribute access)
app.py = app

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
