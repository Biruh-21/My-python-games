import random
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
UP = 90
DOWN = 270
MOVE_DISTANCE = 20

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

player_paddle = Paddle("player")
computer_paddle = Paddle("computer")
ball = Ball()
scoreboard = Scoreboard()

screen.update()

game_is_on = True

def computer_move():
    computer_paddle.computer_paddle.forward(MOVE_DISTANCE)

    if computer_paddle.computer_paddle.ycor() > 245:
        computer_paddle.computer_paddle.setheading(DOWN)
    elif computer_paddle.computer_paddle.ycor() < -230:
        computer_paddle.computer_paddle.setheading(UP)

def up():
    if player_paddle.player_paddle.ycor() < 245:
        player_paddle.player_paddle.setheading(UP)
        player_paddle.player_paddle.forward(MOVE_DISTANCE)

def down():
    if player_paddle.player_paddle.ycor() > -230:
        player_paddle.player_paddle.setheading(DOWN)
        player_paddle.player_paddle.forward(MOVE_DISTANCE)


screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
computer_paddle.computer_paddle.setheading(90)
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    if ball.ycor() > 280 or ball.ycor() < -265:
        init_heading = ball.heading()
        ball.setheading(360 - init_heading)
    if player_paddle.player_paddle.distance(ball) <= 50 and ball.xcor() < -340:
        init_heading = ball.heading()
        ball.move_speed *= 0.9
        if 180 < init_heading < 270:
            ball.setheading((360 - init_heading) + 180)
        elif 90 < init_heading < 180:
            ball.setheading(180 - init_heading)

    elif computer_paddle.computer_paddle.distance(ball) <= 50 and ball.xcor() > 335:
        init_heading = ball.heading()
        if init_heading > 270:
            ball.setheading(180 + (360 - init_heading))
        elif init_heading < 90:
            ball.setheading(90 + (90 - init_heading))

    elif ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()
        ball.move_speed = 0.1
        ball.shape("circle")
        ball.color("white")
        ball.penup()
        ball_to_player = random.randint(110, 250)
        ball.setheading(ball_to_player)
    elif ball.xcor() < -390:
        scoreboard.r_point()
        ball.reset()
        ball.move_speed = 0.1
        ball.shape("circle")
        ball.color("white")
        ball.penup()
        angle_list = []
        ball_to_computer_1 = random.randint(0, 70)
        ball_to_computer_2 = random.randint(290, 360)
        angle_list.append(ball_to_computer_1)
        angle_list.append(ball_to_computer_2)
        angle = random.choice(angle_list)
        ball.setheading(angle)

    ball.forward(20)
    computer_move()

screen.exitonclick()
