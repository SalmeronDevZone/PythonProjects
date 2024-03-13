import random
import pygame
import logging
from io import StringIO

"""
log_stream = StringIO()
logging.basicConfig(stream=log_stream, level=logging.WARNING)"""

pygame.init()


preguntas = [
    {
        "pregunta": "¿En qué película aparece el personaje 'Forrest Gump'?",
        "opciones": ["a) Forrest Gump", "b) El Padrino", "c) Titanic", "d) Matrix"],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Quién dirigió la película 'El Padrino'?",
        "opciones": ["a) Quentin Tarantino", "b) Steven Spielberg", "c) Martin Scorsese", "d) Francis Ford Coppola"],
        "respuesta": "d"
    },
    {
        "pregunta": "¿Cuál es la película con más premios Oscar de la historia?",
        "opciones": ["a) Titanic", "b) El Señor de los Anillos: El Retorno del Rey", "c) La La Land", "d) Ben-Hur"],
        "respuesta": "b"
    }
]

def mostrar_pregunta(pregunta):
    print(pregunta["pregunta"])
    for opcion in pregunta["opciones"]:
        print(opcion)

def jugar():
    puntaje = 0
    random.shuffle(preguntas)
    for pregunta in preguntas:
        mostrar_pregunta(pregunta)
        respuesta_usuario = input("Ingresa tu respuesta (a, b, c, d): ").lower()
        if respuesta_usuario == pregunta["respuesta"]:
            print("¡Respuesta correcta!")
            puntaje += 1
        else:
            print("Respuesta incorrecta.")
    print("Fin del juego. Tu puntaje total es:", puntaje)

if __name__ == "__main__":

    
    print("Bienvenido al juego de preguntas sobre cine!")
    

 
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play()


jugar()
pygame.mixer.music.stop()