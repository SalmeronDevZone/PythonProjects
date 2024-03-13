import random

def obtener_tres_emojis_aleatorios():
    # Diccionario de emojis asociados a números
    emojis = {
        1: "🍎",
        2: "🍏",
        3: "🍐",
        4: "🍑",
        5: "🥭",
        6: "🍆",
        7: "🍅",
        8: "🥝",
        9: "🥥",
        10: "🥑"
    }
    
    # Selecciona tres números aleatorios entre 1 y 10
    numeros_aleatorios = random.choices(list(emojis.keys()), k=3)
    
    # Imprime los emojis correspondientes a los números seleccionados
    emojis_seleccionados = [emojis[numero] for numero in numeros_aleatorios]
    print(" ".join(emojis_seleccionados))
    
    # Verifica si los tres emojis son iguales
    if numeros_aleatorios[0] == numeros_aleatorios[1] == numeros_aleatorios[2]:
        print("¡Has ganado!")

# Llama a la función para obtener y mostrar los tres emojis aleatorios
obtener_tres_emojis_aleatorios()
