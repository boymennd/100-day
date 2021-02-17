from turtle import Screen
from pong_screen import BackGround
from pong_data import Player

screen = Screen()
screen.bgcolor("black")
screen.setup(1000, 600)
screen.title("Welcome to PONG game!")
screen.tracer(0)
screen.listen()
back_ground = BackGround()
back_ground.score_play1()
back_ground.score_play2()
player = Player()
end = False
while not end:
    screen.update()
    player.control()
    player.ball_move()
    player.ball_check()
    if player.goal_p1():
        back_ground.update_p1()
    if player.goal_p2():
        back_ground.update_p2()
screen.exitonclick()
