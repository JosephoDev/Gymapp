from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Monta la carpeta static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configura las plantillas HTML
templates = Jinja2Templates(directory="templates")  # <-- NOTA: sin "PROYECTO/" si estás ejecutando dentro de PROYECTO

# Ruta de login (inicio)
@app.get("/", response_class=HTMLResponse)
async def show_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# ✅ Agrega esta ruta
@app.get("/home", response_class=HTMLResponse)
async def show_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
