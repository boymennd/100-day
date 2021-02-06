from turtle import Turtle
from turtle import Screen
from random import randint

screen = Screen()
color = ["red", "black", "green", "blue", "yellow", "pink", "orange"]
your_turtle = screen.textinput(
    title="Take your turtle",
    prompt="Choose your turtle('red','black','green','blue','yellow','pink''):",
)
screen.setup(height=450, width=750)
y = -208
turtles = []
for turtle_index in range(0, 7):
    turtle = Turtle()
    turtle.penup()
    turtle.shape("turtle")
    turtle.color(color[turtle_index])
    turtle.setx(-350)
    turtle.sety(y)
    turtle.pendown()
    y += 70
    turtles.append(turtle)


def goal():
    t = Turtle()
    t.penup()
    t.sety(220)
    t.setx(333)
    t.pendown()
    t.right(90)
    t.forward(500)


goal()
end = False
while not end:
    for turtle_index in turtles:
        turtle_index.fd(randint(0, 10))
        if turtle_index.xcor() > 333:
            end = True
            if your_turtle.lower() == turtle_index.color()[0]:
                print("You win!!!")
            else:
                b = turtle_index.color()[0]
                print(f"You lose. The {b} turtle win !!!")


screen.exitonclick()
