from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models.connectdb import get_connection
import pymysql

app = FastAPI()

# Monta la carpeta static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configura las plantillas HTML
templates = Jinja2Templates(directory="templates")  

# Ruta de login (inicio)
@app.get("/", response_class=HTMLResponse)
async def show_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def show_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def show_login(request: Request):
    return templates.TemplateResponse("registro.html", {"request": request})

# ✅ Agrega esta ruta
@app.get("/home", response_class=HTMLResponse)
async def show_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/IMC", response_class=HTMLResponse)
async def show_home(request: Request):
    return templates.TemplateResponse("IMC.html", {"request": request})

@app.post("/register")
async def register_user(name: str = Form(...), password: str = Form(...)):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = "INSERT INTO users (username, psw) VALUES (%s, %s)"
        cursor.execute(query, (name, password))

        connection.commit()

        cursor.close()
        connection.close()

        return {"message": "Usuario registrado exitosamente"}
    
    except pymysql.MySQLError as e:
        return {"error": str(e)}
    
@app.post("/login")
async def login_user(name: str = Form(...), password: str = Form(...)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = %s AND psw = %s"
        cursor.execute(query, (name, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            return {"message": f"Bienvenido, {user['username']}"}
        else:
            return JSONResponse(status_code=401, content={"error": "Usuario o contraseña incorrectos"})

    except pymysql.MySQLError as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
