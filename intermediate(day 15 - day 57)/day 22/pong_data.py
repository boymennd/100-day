from turtle import Turtle, Screen
from random import randint

screen = Screen()
a = randint(145, 205)


class Player:
    def __init__(self):
        self.ball = Turtle()
        self.turtle_p1 = Turtle()
        self.turtle_p2 = Turtle()
        self.player1()
        self.player2()
        self.balls()
        self.x_move = 0.5
        self.y_move = 0.5

    def player1(self):
        self.turtle_p1.penup()
        self.turtle_p1.color("white")
        self.turtle_p1.shape("square")
        self.turtle_p1.goto(-470, 0)
        self.turtle_p1.shapesize(5, 1)

    def player2(self):
        self.turtle_p2.penup()
        self.turtle_p2.color("white")
        self.turtle_p2.shape("square")
        self.turtle_p2.goto(470, 0)
        self.turtle_p2.shapesize(5, 1)

    def up_p1(self):
        self.turtle_p1.goto(self.turtle_p1.xcor(), self.turtle_p1.ycor() + 30)

    def up_p2(self):
        self.turtle_p2.goto(self.turtle_p2.xcor(), self.turtle_p2.ycor() + 30)

    def down_p1(self):
        self.turtle_p1.goto(self.turtle_p1.xcor(), self.turtle_p1.ycor() - 30)

    def down_p2(self):
        self.turtle_p2.goto(self.turtle_p2.xcor(), self.turtle_p2.ycor() - 30)

    def control(self):
        screen.onkey(self.up_p1, "w")
        screen.onkey(self.down_p1, "s")
        screen.onkey(self.up_p2, "Up")
        screen.onkey(self.down_p2, "Down")

    def balls(self):
        self.ball.penup()
        self.ball.color("white")
        self.ball.shape("circle")
        self.ball.setheading(a)

    def ball_move(self):
        new_x = self.ball.xcor() - self.x_move
        new_y = self.ball.ycor() - self.y_move
        self.ball.goto(new_x, new_y)

    def ball_check(self):
        if self.ball.ycor() > 280 or self.ball.ycor() < -280:
            self.y_move *= -1

    def ball_check_p1(self):
        y_p1 = self.turtle_p1.ycor()
        if (
            y_p1 - 50 <= self.ball.ycor() <= y_p1 + 50
            and self.ball.xcor() == self.turtle_p1.xcor() + 10
        ):
            self.x_move *= -1
            return True

    def ball_check_p2(self):
        y_p2 = self.turtle_p2.ycor()
        if (
            y_p2 - 50 <= self.ball.ycor() <= y_p2 + 50
            and self.ball.xcor() == self.turtle_p2.xcor() - 10
        ):
            self.x_move *= -1
            return True

    def end_game(self):
        if self.ball.xcor() > 500 or self.ball.xcor() < -500:
            print("Game over!!!")
            return True
