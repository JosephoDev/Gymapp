from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
from app.models.linear_regression import LinearRegression
from app.utils.data_simulation import generate_dataset
import matplotlib.pyplot as plt
import numpy as np
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

model = LinearRegression()

class PredictRequest(BaseModel):
    input_data: List[float]

@app.on_event("startup")
async def startup_event():
    X, y = generate_dataset()
    model.fit(X, y)
    generate_plot(X, y, model)

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/train")
def train_model():
    X, y = generate_dataset()
    model.fit(X, y)
    generate_plot(X, y, model)
    return {"message": "Model trained successfully"}

@app.post("/predict")
def predict(request: PredictRequest):
    input_data = request.input_data
    prediction = model.predict(input_data)
    return {"prediction": prediction.tolist()}

@app.get("/plot")
def get_plot():
    return FileResponse("app/static/plot.png")

def generate_plot(X, y, model):
    plt.scatter(X, y, color='blue', label='Data points')
    X_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    y_line = model.predict(X_line)
    plt.plot(X_line, y_line, color='red', label='Regression line')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.savefig("app/static/plot.png")
    plt.close()
    print("Plot generated and saved as app/static/plot.png")