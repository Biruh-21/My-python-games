import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard(True)


screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() >= 280:
        scoreboard.level += 1
        car_manager.speed_up(scoreboard.level)
        scoreboard.next_level()
        player.reset()
        player.penup()
        player.goto(0, -280)
        player.setheading(90)
    car_manager.create_car()
    for car in car_manager.all_cars:
        if car.distance(player) < 23:
            scoreboard.game_over()
            game_is_on = False
        car.forward(car_manager.car_speed)
        # print(car_manager.car_speed)

screen.exitonclick()