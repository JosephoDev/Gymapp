from models.connectdb import get_connection

def recommend_exercises(imc, tipo, objetivo):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            SELECT name, description
            FROM exercises
            WHERE %s BETWEEN imc_min AND imc_max
              AND type = %s
              AND goal = %s
        """
        cursor.execute(query, (imc, tipo, objetivo))
        results = cursor.fetchall()

        cursor.close()
        conn.close()
        return results

    except Exception as e:
        return []