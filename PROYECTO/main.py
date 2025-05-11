from fastapi import FastAPI, Request, Form, Body
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models.connectdb import get_connection
from models.exercise import recommend_exercises
from models.food import recommend_food
import pymysql

app = FastAPI()

# Monta la carpeta static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configura las plantillas HTML
templates = Jinja2Templates(directory="templates")  

# Definir Usuario
class UserUpdateData(BaseModel):
    username: str
    imc: float
    tipo: int
    objetivo: int
    
# Modificar Usuario 
@app.post("/update_user_data")
async def update_user_data(data: UserUpdateData):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = "UPDATE users SET IMC = %s, type = %s, goal = %s WHERE username = %s"
        cursor.execute(query, (data.imc, data.tipo, data.objetivo, data.username))

        conn.commit()
        cursor.close()
        conn.close()

        return {"message": "Datos actualizados correctamente"}

    except Exception as e:
        return {"error": str(e)}

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

# ✅ Agrega esta ruta
@app.get("/about", response_class=HTMLResponse)
async def show_home(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# ✅ Agrega esta ruta
@app.get("/contact", response_class=HTMLResponse)
async def show_home(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})
                                      
@app.get("/IMC", response_class=HTMLResponse)
async def show_home(request: Request):
    return templates.TemplateResponse("IMC.html", {"request": request})

@app.get("/train", response_class=HTMLResponse)
async def show_home(request: Request):
    return templates.TemplateResponse("train.html", {"request": request})

@app.get("/food", response_class=HTMLResponse)
async def show_home(request: Request):
    return templates.TemplateResponse("food.html", {"request": request})

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
    
@app.get("/train", response_class=HTMLResponse)
async def show_exercises(request: Request):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Suponiendo que tienes un usuario logueado (por ejemplo guardado en localStorage en JS y enviado como parámetro)
        username = request.query_params.get("username")  # O ajústalo como prefieras
        if not username:
            return templates.TemplateResponse("train.html", {"request": request, "exercises": [], "error": "Usuario no autenticado"})

        # Obtener los datos del usuario
        cursor.execute("SELECT IMC, type, goal FROM users WHERE username = %s", (username,))
        user_data = cursor.fetchone()

        cursor.close()
        conn.close()

        if not user_data:
            return templates.TemplateResponse("train.html", {"request": request, "exercises": [], "error": "Datos del usuario no encontrados"})

        # Obtener ejercicios recomendados
        from models.exercise import recommend_exercises
        exercises = recommend_exercises(user_data['IMC'], user_data['type'], user_data['goal'])

        return templates.TemplateResponse("train.html", {"request": request, "exercises": exercises, "error": None})

    except Exception as e:
        return templates.TemplateResponse("train.html", {"request": request, "exercises": [], "error": str(e)})