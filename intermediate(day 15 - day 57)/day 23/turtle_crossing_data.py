from turtle import Turtle, Screen

screen = Screen()


class YourTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.goto(0, -280)
        self.pen = Turtle()
        self.lever = 1

    def levers(self):
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(-240, 250)
        self.pen.write(
            f"Lever:{self.lever}", True, "center", font=("Arial", 18, "normal")
        )

    def lever_update(self):
        self.pen.clear()
        self.pen.goto(-240, 250)
        self.pen.write(
            f"Lever:{self.lever}", True, "center", font=("Arial", 18, "normal")
        )

    def end_game(self):
        self.pen.goto(0, 0)
        self.pen.write("GAME OVER!!", True, "center", font=("Arial", 25, "normal"))

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def control(self):
        screen.onkey(self.up, "w")
        screen.onkey(self.down, "s")

    def next_step(self):
        if self.ycor() == 260:
            self.lever += 1
            self.goto(0, -280)
            self.lever_update()
            return True
