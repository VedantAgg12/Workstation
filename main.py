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

@app.get("/dashboard")
async def dashboard(request: Request):
    config = database.get_config()
    username = config.get("username", "User") if config else "User"
    modules = database.get_modules()
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "username": username,
        "modules": modules
    })

@app.post("/setup")
async def setup(request: Request, username: str = Form(...)):
    database.create_config(username)
    return RedirectResponse(url="/", status_code=303)

@app.get("/workspaces")
async def workspaces(request: Request):
    config = database.get_config()
    if not config:
        return RedirectResponse(url="/")
    
    workspaces_data = database.get_workspaces()
    return templates.TemplateResponse("workspaces.html", {
        "request": request, 
        "username": config.get("username", "User"),
        "workspaces": workspaces_data
    })

@app.get("/api/modules")
async def get_modules():
    return database.get_modules()

@app.post("/api/workspaces")
async def add_workspace(request: Request):
    data = await request.json()
    return database.add_workspace(data)

# Hack to support 'uvicorn main:app.py' (uvicorn treats dots as attribute access)
app.py = app

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
