from turtle import Screen, Turtle
from turtle_crossing_data import YourTurtle
from auto_car import AutoCar
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
turtle = YourTurtle()
auto_car = AutoCar()
auto_car.the_car()
screen.listen()
turtle.levers()
end = False
while not end:
    screen.update()
    time.sleep(0.1)
    turtle.control()
    auto_car.car_move()
    if turtle.next_step():
        auto_car.x_move += 1
        auto_car.appen_car()
    for car in auto_car.car_list:
        if turtle.distance(car) < 17:
            end = True
            turtle.end_game()


screen.exitonclick()
