import random

def obtener_tres_emojis_aleatorios():
    # Lista de emojis
    emojis = ["🍎", "🍏", "🍐", "🍑", "🥭", "🍆", "🍅", "🥝", "🥥", "🥑"]
    
    # Selecciona tres emojis al azar de la lista
    random_emojis = random.choices(emojis, k=3)
    
    # Imprime los tres emojis seleccionados
    print(" ".join(random_emojis))
    
    # Verifica si los tres emojis son iguales
    if random_emojis[0] == random_emojis[1] == random_emojis[2]:
        print("¡Has ganado!")

# Llama a la función para obtener y mostrar los tres emojis aleatorios
        
# obtener_tres_emojis_aleatorios()

"""emojis = {
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
 """

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

print(emojis[1])


import random

# Definir los símbolos
simbolos = ["Cereza", "Naranja", "Limón", "Ciruela", "Campana", "Siete"]

# Definir el valor de cada símbolo
valores = {
    "Cereza": 1,
    "Naranja": 2,
    "Limón": 3,
    "Ciruela": 4,
    "Campana": 5,
    "Siete": 7, #7️⃣
}

# Función para tirar los dados
def tirar_dados():
    return [random.choice(simbolos) for _ in range(3)]

# Función para calcular el pago
def calcular_pago(dados):
    # Si hay tres símbolos iguales, se paga el valor del símbolo multiplicado por 3
    if dados[0] == dados[1] == dados[2]:
        return valores[dados[0]] * 3
    # Si hay dos símbolos iguales, se paga el valor del símbolo multiplicado por 2
    elif dados[0] == dados[1] or dados[0] == dados[2] or dados[1] == dados[2]:
        return valores[dados[0]] * 2
    # Si no hay ningún símbolo igual, se pierde
    else:
        return 0

# Función para jugar una partida
def jugar_partida():
    # Tirar los dados
    dados = tirar_dados()

    # Calcular el pago
    pago = calcular_pago(dados)

    # Mostrar el resultado
    print("Tirada:", dados)
    if pago > 0:
        print("¡Has ganado", pago, "monedas!")
    else:
        print("Has perdido.")

# Jugar una partida
jugar_partida()

# Preguntar al usuario si quiere jugar otra partida
while True:
    respuesta = input("¿Quieres jugar otra partida? (s/n) ")
    if respuesta.lower() == "s":
        jugar_partida()
    else:
        break