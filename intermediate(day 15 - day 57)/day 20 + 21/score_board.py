from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(0,255)

    def score_up(self,scores):
        self.write(f"Score: {scores}", True, "center", font=("Arial", 18, "normal"))
    def game_over(self,scores):
        self.goto(0,0)
        self.write("GAME OVER !!",True,"center",font=("Arial", 18, "normal"))
        self.goto(0,-15)
        self.write(f"your final score: {scores}",True,"center")