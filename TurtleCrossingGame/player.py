from turtle import Turtle
from scoreboard import Scoreboard
from car_manager import CarManager
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

car_manager = CarManager()


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):


        self.forward(MOVE_DISTANCE)



