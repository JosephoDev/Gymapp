import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="proyecto",
        cursorclass=pymysql.cursors.DictCursor  # Opcional: devuelve resultados como diccionario
    )
