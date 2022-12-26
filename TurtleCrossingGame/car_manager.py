import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 8


class CarManager:
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_car(self):
        rand_chance = random.randint(1,6)
        if rand_chance == 1:
            car = Turtle(shape="square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.penup()
            y_pos = random.randint(-250, 250)
            car.goto(280, y_pos)
            self.all_cars.append(car)

    def speed_up(self, level):
        print(level)
        self.car_speed = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (level - 1))
        print(self.car_speed)



