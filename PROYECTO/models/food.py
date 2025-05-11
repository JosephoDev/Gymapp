def recommend_food(imc: float, tipo: int, objetivo: int) -> list[str]:
    comidas = []

    if imc < 18.5:
        comidas = ["Aumentar calorías con proteínas", "Batidos hipercalóricos", "Frutos secos, arroz, aguacate"]
    elif 18.5 <= imc < 25:
        if objetivo == 1:
            comidas = ["Déficit calórico", "Verduras, proteínas magras", "Evita azúcares"]
        elif objetivo == 2:
            comidas = ["Proteínas altas", "Carbohidratos complejos", "Comer cada 3-4 horas"]
        elif objetivo == 3:
            comidas = ["Alto en proteína", "Bajo en carbohidratos", "Poca sal"]
    elif 25 <= imc < 30:
        comidas = ["Control de porciones", "Comidas ligeras", "Aumentar vegetales"]
    else:
        comidas = ["Plan bajo en grasas y azúcares", "Evitar fritos", "Beber mucha agua"]

    return comidas
