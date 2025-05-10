from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Monta la carpeta static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configura las plantillas HTML
templates = Jinja2Templates(directory="templates")  

# Ruta de login (inicio)
@app.get("/", response_class=HTMLResponse)
async def show_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# ✅ Agrega esta ruta
@app.get("/home", response_class=HTMLResponse)
async def show_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# ✅ Agrega esta ruta
@app.get("/about", response_class=HTMLResponse)
async def show_home(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# ✅ Agrega esta ruta
@app.get("/contact", response_class=HTMLResponse)
async def show_home(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

# ✅ Agrega esta ruta
@app.get("/home", response_class=HTMLResponse)
async def show_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
