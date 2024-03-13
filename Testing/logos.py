# Logo Tecnológico con Microchips y Lenguajes de Programación
import turtle as t

# Configuración
t.bgcolor("black")
t.speed(0)
t.pensize(2)

# Dibujo del Microchip
t.color("cyan")
t.begin_fill()
for _ in range(6):
    t.forward(50)
    t.right(60)
t.end_fill()

# Dibujo de los Lenguajes de Programación
languages = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go"]
colors = ["red", "green", "blue", "yellow", "purple", "orange"]

for i, lang in enumerate(languages):
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.color(colors[i])
    t.goto(30, -20 - i * 20)
    t.pendown()
    t.write(lang, align="left", font=("Arial", 10, "bold"))

# Ocultar la tortuga
t.hideturtle()

# Mostrar el logo
t.done()
