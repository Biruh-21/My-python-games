from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        rand_pos = random.randint(-250, 250)
        angle_list = []
        rand_angle_1 = random.randint(0, 70)
        rand_angle_2 = random.randint(290, 360)
        rand_angle_3 = random.randint(110, 250)
        angle_list.append(rand_angle_1)
        angle_list.append(rand_angle_2)
        angle_list.append(rand_angle_3)
        angle = random.choice(angle_list)
        self.sety(rand_pos)
        self.setheading(angle)
        self.move_speed = 0.1

