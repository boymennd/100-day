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
the_score.score_up()
end = False
while not end:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.check():
        the_score.scores += 1
        the_score.update_score()
    snake.colors()
    if snake.over_wall() or snake.die_your_self():
        snake.reset()
        the_score.reset()
























screen.exitonclick()