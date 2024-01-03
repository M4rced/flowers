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
turtle.bgcolor("black")
turtle.shape("turtle")
turtle.speed(0)
turtle.fillcolor("brown")

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

# Dibuja hojas en el tallo (ubicadas en la mitad del tallo verticalmente)
turtle.penup()
turtle.goto(0, -250)
turtle.pendown()
draw_leaf(40, "green")

turtle.penup()
turtle.goto(-20, -280)
turtle.pendown()
draw_leaf(30, "green")

turtle.penup()
turtle.goto(20, -280)
turtle.pendown()
draw_leaf(30, "green")

# Cambia el color del centro del girasol a blanco
turtle.penup()
turtle.goto(0, -180)
turtle.fillcolor("#8B4513")
turtle.begin_fill()
turtle.circle(0)
turtle.end_fill()

# Código del girasol (el que proporcionaste)
phi = 137.508 * (math.pi / 180.0)
for i in range(160 + 40):
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
        turtle.fillcolor("yellow")  # Cambia el color de las hojas
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
turtle.color("white")  # Color del texto
turtle.write("Feliz Año, Majo❤️", align="center", font=("Cambria", 24, "italic"))

# Oculta el cursor de la tortuga antes de salir
turtle.hideturtle()

# Cierra la ventana al hacer clic
turtle.exitonclick()