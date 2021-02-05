import turtle as t
from turtle import Screen
from random import randint

turtle = t.Turtle()
t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    t = (r, g, b)
    return t


turtle.penup()
y = -200
while y < 200:
    turtle.setx(-400)
    turtle.sety(y)
    for _ in range(20):
        turtle.speed(500)
        turtle.fd(20)
        turtle.dot(20, random_color())
        turtle.fd(20)
    turtle.home()
    y += 40
screen = Screen()
screen.exitonclick()
