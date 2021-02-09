from turtle import Screen
from snake_data import Snake
from score_board import ScoreBoard
import time
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Welcome to snake game")
screen.tracer(0)
snake = Snake()
the_score = ScoreBoard()
screen.listen()
snake.control()
snake.point()
score = 0
the_score.score_up(score)
end = False
while not end:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.check():
        the_score.clear()
        the_score.goto(0,255)
        score += 1
        the_score.score_up(score)
    snake.colors()
    if snake.over_wall() or snake.die_your_self():
        end = True
        the_score.game_over(score)
























screen.exitonclick()