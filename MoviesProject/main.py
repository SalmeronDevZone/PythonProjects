import pygame
import os
import random
from conexion import obtener_preguntas, conectar_bd

""" MÚSICA """
pygame.init()
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play()

def hacer_pregunta(conexion):
    # Obtener preguntas desde la base de datos
    preguntas = obtener_preguntas(conexion)
    
    if preguntas:
        # Seleccionar una pregunta aleatoria
        pregunta = random.choice(preguntas)
        print("Pregunta:", pregunta)
        respuesta = input("Respuesta: ")

        # Aquí iría la lógica para verificar la respuesta y actualizar los puntos
    else:
        print("No hay preguntas disponibles.")

def main():
    print("¡Bienvenido a Cinemáticamente RICO!")
    nombre_jugador = input("Por favor, introduce tu nombre: ")
    puntos = 100000
    print(f"Bienvenido, {nombre_jugador}! Empiezas con {puntos} puntos. Estás preparado para ser millonario!") 

    # Establecer conexión a la base de datos
    conexion = conectar_bd()

    if conexion:
        # Hacer una pregunta
        hacer_pregunta(conexion)
        conexion.close()

if __name__ == "__main__":
    main()

