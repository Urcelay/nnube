import math
from turtle import *
import turtle
import pygame
from pygame import mixer
pygame.init()
mixer.init()
mixer.music.load('C:/Users/ferna/OneDrive/Documentos/juego de python/__pycache__/audiobonito.mp3')
mixer.music.play(-1)

#------------------------------------------------------------------
def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * \
        math.cos(2 * k) - 2 * \
        math.cos(3 * k) - \
        math.cos(4 * k)

# Configuración de la pantalla
turtle.speed(0)
turtle.bgcolor("black")
turtle.color('red')

def dibujar_corazon(scale, offset_x, offset_y):
    penup()
    for i in range(300):
        x = hearta(i) * scale + offset_x
        y = heartb(i) * scale + offset_y
        goto(x, y)
        pendown()
    penup()

# Coordenadas para los corazones a la izquierda y a la derecha
# Corazones a la izquierda
offsets_izquierda = [(-300, 100), (-300, 0), (-300, -100)]
# Corazones a la derecha
offsets_derecha = [(200, 100), (200, 0), (200, -100)]

# Dibujar corazones a la izquierda
for offset in offsets_izquierda:
    dibujar_corazon(1, *offset)

# Dibujar corazones a la derecha
for offset in offsets_derecha:
    dibujar_corazon(1, *offset)

# Función para dibujar el ojo izquierdo
def ojo_izquierdo():
    turtle.bgcolor('black')
    turtle.pencolor('pink')
    turtle.speed(0)  # Velocidad máxima para dibujar rápidamente

    turtle.penup()  # Levantamos
    turtle.goto(-200, 200)  # Cambiamos la posición
    turtle.pendown()  # Bajamos tortuga
    size = 100
    decremento = 2  # Se rellena la orilla del ojo

    for i in range(10):  # Se dibujan 10 cuadrados
        for _ in range(4):  # 4 lados
            turtle.forward(size)
            turtle.right(90)
        size -= decremento
        
        # Ajustar la posición de la tortuga para centrar el próximo cuadrado
        turtle.penup()
        turtle.forward(decremento / 2)
        turtle.right(90)
        turtle.forward(decremento / 2)
        turtle.left(90)
        turtle.pendown()

    turtle.penup()
    turtle.color('white')
    turtle.goto(-175, 170)
    turtle.down()
    size2 = 25
    for a in range(16):  # Parte cuadrado blanco OJO
        for b in range(4):
            turtle.forward(size2)
            turtle.right(90)
        size2 -= decremento
        turtle.penup()
        turtle.forward(decremento / 2)
        turtle.right(90)
        turtle.forward(decremento / 2)
        turtle.left(90)
        turtle.pendown()

    turtle.penup()
    turtle.goto(-135, 150)
    turtle.down()
    size3 = 10
    size4 = 18
    for rec in range(7):
        for rec2 in range(4):
            turtle.forward(size3)
            turtle.right(90)
            turtle.forward(size4)
            turtle.right(90)
        size3 -= decremento
        size4 -= decremento
        turtle.penup()
        turtle.forward(decremento / 2)
        turtle.right(90)
        turtle.forward(decremento / 2)
        turtle.left(90)
        turtle.pendown()
    turtle.hideturtle()

# Función para dibujar el ojo derecho
def ojo_derecho():
    tortuga2 = turtle.Turtle()
    tortuga2.color('pink')
    tortuga2.speed(0)

    tortuga2.penup()
    tortuga2.goto(30, 200)
    tortuga2.pendown()
    size = 100
    decremento = 2  # Se rellena la orilla del ojo

    for i in range(10):  # Se dibujan 10 cuadrados
        for _ in range(4):  # 4 lados
            tortuga2.forward(size)
            tortuga2.right(90)
        size -= decremento
        
        # Ajustar la posición de la tortuga para centrar el próximo cuadrado
        tortuga2.penup()
        tortuga2.forward(decremento / 2)
        tortuga2.right(90)
        tortuga2.forward(decremento / 2)
        tortuga2.left(90)
        tortuga2.pendown()

    tortuga2.penup()
    tortuga2.color('white')
    tortuga2.goto(60, 170)
    tortuga2.down()
    size2 = 25
    for a in range(14):  # Parte cuadrado blanco OJO
        for b in range(4):
            tortuga2.forward(size2)
            tortuga2.right(90)
        size2 -= decremento
        tortuga2.penup()
        tortuga2.forward(decremento / 2)
        tortuga2.right(90)
        tortuga2.forward(decremento / 2)
        tortuga2.left(90)
        tortuga2.pendown()

    tortuga2.penup()
    tortuga2.goto(95, 150)
    tortuga2.down()
    size5 = 10
    size6 = 18
    for rec in range(7):
        for rec2 in range(4):
            tortuga2.forward(size5)
            tortuga2.right(90)
            tortuga2.forward(size6)
            tortuga2.right(90)
        size5 -= decremento
        size6 -= decremento
        tortuga2.penup()
        tortuga2.forward(decremento / 2)
        tortuga2.right(90)
        tortuga2.forward(decremento / 2)
        tortuga2.left(90)
        tortuga2.pendown()
    tortuga2.hideturtle()

# Función para dibujar el cuerpo
def cuerpo():
    tortuga3 = turtle.Turtle()
    tortuga3.color('pink')
    tortuga3.speed(0)
    tortuga3.penup()
    tortuga3.goto(-180, 85)  # Posición inicial para el cuerpo
    tortuga3.pendown()
    size7 = 290
    decremento4 = 2

    tortuga3.begin_fill()  # Inicia el relleno
    for cuadrado2 in range(4):
        tortuga3.forward(size7)
        tortuga3.right(90)
    tortuga3.end_fill()  # Termina el relleno
    tortuga3.hideturtle()

# Función para dibujar la boca
def boca():
    tortuga4 = turtle.Turtle()
    tortuga4.color('black')
    tortuga4.speed(0)
    tortuga4.penup()
    tortuga4.goto(-80, 20)
    tortuga4.pendown()
    size8 = 80
    size9 = 20
    decremento = 2
    for rectangulo in range(12):
        for rectangulo2 in range(4):
            tortuga4.forward(size8)
            tortuga4.right(90)
            tortuga4.forward(size9)
            tortuga4.right(90)
        size8 -= decremento
        size9 -= decremento
        tortuga4.penup()
        tortuga4.forward(decremento / 2)
        tortuga4.right(90)
        tortuga4.forward(decremento / 2)
        tortuga4.left(90)
        tortuga4.pendown()
    tortuga4.hideturtle()

# Función para agregar texto
def letras():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.color('white')

    screen_width, screen_height = turtle.screensize()
    t.goto(screen_width - 500, screen_height - 50)
    t.write('PARA MI KIWI...', align='right', font=('Garamond', 20, 'italic'))

    t.goto(50, -250)
    t.write('AYU HEMBRA VIRTUAL 14/08/2024', align='center', font=('Garamond', 20, 'italic'))

# Llamado a las funciones para dibujar cada parte
dibujar_corazon(1, -300, 100) 
ojo_izquierdo()
ojo_derecho()
cuerpo()
boca()
letras()

turtle.done()
