from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_pos = (random.randint(-280, 280), random.randint(-280, 280))
        self.goto(random_pos)

    def refresh(self):
        random_pos = (random.randint(-280, 280), random.randint(-280, 280))
        self.goto(random_pos)
