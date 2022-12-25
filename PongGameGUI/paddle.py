from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle:
    def __init__(self, paddle):
        if paddle == "player":
            self.player_paddle = self.create_player_paddle()
        elif paddle == "computer":
            self.computer_paddle = self.create_computer_paddle()

    def create_paddle(self, x_pos):
        one_sqr = Turtle(shape="square")
        one_sqr.penup()
        one_sqr.color("white")
        one_sqr.shapesize(stretch_wid=1, stretch_len=5)
        one_sqr.setheading(90)
        one_sqr.setposition(x_pos, 0)
        return one_sqr

    def create_player_paddle(self):
        paddle = self.create_paddle(-370)
        return paddle

    def create_computer_paddle(self):
        paddle = self.create_paddle(360)
        return paddle




