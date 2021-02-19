from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(0,255)

    def score_up(self):
        self.write(f"Score: {self.scores}   High score: {self.high_score}", True, "center", font=("Arial", 18, "normal"))

    def update_score(self):
        self.clear()
        self.goto(0,255)
        self.score_up()

    def reset(self):
        if self.scores > self.high_score:
            self.high_score = self.scores
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.scores = 0
        self.update_score()
