import math
import turtle

def draw_leaf(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(30)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(30)
    turtle.forward(size)
    turtle.end_fill()

# Configuración inicial
turtle.bgcolor("#00BFFF")
turtle.shape("turtle")
turtle.speed(0)
turtle.fillcolor("yellow")

# Dibuja el tallo


turtle.penup()
turtle.goto(0, -300)
turtle.pendown()
turtle.setheading(90)
turtle.fillcolor("green")  # Cambia el color del tallo a verde
turtle.begin_fill()
turtle.forward(200)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(200)
turtle.end_fill()

# Cambia el color del centro del girasol a blanco
turtle.penup()
turtle.goto(0, -180)
turtle.fillcolor("yellow")  # brown
turtle.begin_fill()
turtle.circle(0)
turtle.end_fill()

# Código del girasol (el que proporcionaste)
phi = 137.508 * (math.pi / 180.0)
for i in range(160 + 21):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    if i < 160:
        turtle.stamp()
    else:
        turtle.fillcolor("white")  # Cambia el color de las hojas
        turtle.begin_fill()
        turtle.right(20)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.left(140)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.end_fill()


turtle.penup()
turtle.goto(0, 200)  # Ajusta la posición vertical según sea necesario
turtle.color("yellow")  # Color del texto
turtle.write("Buen día, Majo ☀️", align="center", font=("Impact", 24, "italic"))

# Oculta el cursor de la tortuga antes de salir
turtle.hideturtle()

# Cierra la ventana al hacer clic
turtle.exitonclick()