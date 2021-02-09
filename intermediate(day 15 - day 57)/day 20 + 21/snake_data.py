from turtle import Turtle,Screen
from random import randint
screen = Screen()
start_pos = [(0, 0), (-20, 0), (-40, 0)]
up = 90
down = 270
right = 0
left = 180
your_score = 0
class Snake:
    def __init__(self):
        self.snakes = []
        self.add_snake()
        self.head = self.snakes[0]
    def add_snake(self):
        for pos in start_pos:
            turtle = Turtle()
            turtle.penup()
            turtle.goto(pos)
            turtle.color("white")
            turtle.shape("square")
            self.snakes.append(turtle)
    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            x_cor = self.snakes[i-1].xcor()
            y_cor = self.snakes[i-1].ycor()
            self.snakes[i].goto(x_cor, y_cor)
        self.snakes[0].forward(20)
    def up(seft):
        if seft.head.heading() != down:
            seft.head.setheading(up)

    def right(seft):
        if seft.head.heading() != left:
            seft.head.setheading(right)

    def left(seft):
        if seft.head.heading() != right:
            seft.head.setheading(left)

    def down(seft):
        if seft.head.heading() != up:
            seft.head.setheading(down)

    def control(self):
        screen.onkey(self.right, "d")
        screen.onkey(self.left, "a")
        screen.onkey(self.up, "w")
        screen.onkey(self.down, "s")
    def point(self):
        self.point = Turtle()
        self.point.penup()
        self.point.shape("circle")
        self.point.shapesize(0.5,0.5)
        self.point.color("blue")
        self.point.setx(randint(-290, 290))
        self.point.sety(randint(-290, 290))
        self.check()
    def check(self):
        c = len(self.snakes)
        if self.snakes[0].distance(self.point) < 15:
            turtle = Turtle()
            turtle.penup()
            turtle.color("White")
            turtle.shape("square")
            turtle.setx(self.snakes[c - 1].xcor() - 10)
            turtle.sety(self.snakes[c - 1].ycor() - 10)
            self.snakes.append(turtle)
            self.point.setx(randint(-280,280))
            self.point.sety(randint(-280,280))
            return True
    def colors(self):
        for snake in self.snakes[0:len(self.snakes):2]:
            snake.color("green")
    def over_wall(self):
        if self.snakes[0].xcor() >= 300 or self.snakes[0].ycor() >= 300:
            print("Game over!!!")
            return True
        if self.snakes[0].xcor() <= -300 or self.snakes[0].ycor() <= -300:
            print("Game over!!!")
            return True
    def die_your_self(self):
        for snake in self.snakes[1:]:
            if self.snakes[0].distance(snake) < 10:
                print("Game over !!!")
                return True