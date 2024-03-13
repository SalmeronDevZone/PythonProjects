import mysql.connector


def conectar_bd():
    
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            database="preguntas_peliculas"  
        )
        #print("Conexión establecida.")
        return conexion
    
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None

def obtener_preguntas(conexion):
    
    preguntas = []
    if conexion:
        try:
            cursor = conexion.cursor()

            cursor.execute("SELECT pregunta, falso_uno, falso_dos, respuesta FROM preguntas")

            for pregunta, falso_uno, falso_dos, respuesta in cursor:
                preguntas.append({"pregunta": pregunta, "falso_uno": falso_uno, "falso_dos": falso_dos, "respuesta": respuesta})
            cursor.close()

            return preguntas
        
        except mysql.connector.Error as error:
            print("Error al obtener preguntas de la base de datos:", error)
            
    else:
        print("No se puede obtener preguntas. Caida de la conexión")
        return None

if __name__ == "__main__":
    conexion = conectar_bd()
    if conexion:
        preguntas = obtener_preguntas(conexion)
        if preguntas:
            print("Preguntas obtenidas de la base de datos:")
            for pregunta in preguntas:
                print(pregunta)
        conexion.close()
