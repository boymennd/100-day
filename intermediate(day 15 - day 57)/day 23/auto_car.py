import turtle as t
from random import randint, choice

car_color = ["red", "black", "blue", "yellow", "orange", "pink", "green"]
xcor_car = [
    -300,
    -260,
    -220,
    -180,
    -140,
    -100,
    -60,
    -20,
    20,
    60,
    100,
    140,
    180,
    220,
    260,
    300,
    340,
    380,
    420,
    460,
    500,
]
ycor_car = [230, 184, 138, 92, 46, 0, -46, -92, -138, -184, -230]


class AutoCar:
    def __init__(self):
        self.car_list = []
        self.x_move = 8

    def the_car(self):
        for i in range(12):
            car = t.Turtle()
            t.colormode(255)
            car.penup()
            car.shape("square")
            car.color(randint(0, 255), randint(0, 255), randint(0, 255))
            car.shapesize(1, 2)
            car.goto(choice(xcor_car), choice(ycor_car))
            self.car_list.append(car)

    def appen_car(self):
        for i in range(3):
            car = t.Turtle()
            t.colormode(255)
            car.penup()
            car.shape("square")
            car.color(randint(0, 255), randint(0, 255), randint(0, 255))
            car.shapesize(1, 2)
            car.goto(randint(-380, 500), randint(-230, 230))
            self.car_list.append(car)

    def car_move(self):
        for car in self.car_list:
            new_x = car.xcor() - self.x_move
            car.goto(new_x, car.ycor())
            if car.xcor() < -500:
                car.goto(500, car.ycor())
