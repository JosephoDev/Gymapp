from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_form(request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(name: str = Form(...), psw: str = Form(...)):
    # Validación: el nombre de usuario solo puede contener letras mayúsculas y minúsculas
    if not name.isalpha():
        raise HTTPException(status_code=400, detail="El nombre de usuario solo puede contener letras mayúsculas y minúsculas.")

    # Aquí puedes agregar la lógica para verificar si el usuario y la contraseña son correctos
    # if usuarioExiste(name, psw):
    #     return {"message": "Inicio de Sesión Completado."}
    # else:
    #     raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos.")

    return {"message": "Inicio de Sesión Completado."}