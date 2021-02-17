from turtle import Turtle


class BackGround(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pensize(5)
        self.hideturtle()
        self.pencolor("white")
        self.speed(200)
        self.middle_line()
        self.score_p1 = 0
        self.score_p2 = 0

    def middle_line(self):
        self.goto(0, 300)
        self.setheading(270)
        for _ in range(15):
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(20)

    def score_play1(self):
        self.goto(-40, 240)
        self.write(self.score_p1, True, "center", font=("Arial", 40, "normal"))

    def score_play2(self):
        self.goto(40, 240)
        self.write(self.score_p2, True, "center", font=("Arial", 40, "normal"))

    def update_p1(self):
        self.score_p1 += 1
        self.clear()
        self.middle_line()
        self.goto(-40, 240)
        self.write(self.score_p1, True, "center", font=("Arial", 40, "normal"))
        self.goto(40, 240)
        self.write(self.score_p2, True, "center", font=("Arial", 40, "normal"))

    def update_p2(self):
        self.score_p2 += 1
        self.clear()
        self.middle_line()
        self.goto(-40, 240)
        self.write(self.score_p1, True, "center", font=("Arial", 40, "normal"))
        self.goto(40, 240)
        self.write(self.score_p2, True, "center", font=("Arial", 40, "normal"))

