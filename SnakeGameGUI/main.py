from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import  Scoreboard
import time

# TODO: 1, create a snake body
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()


segments = snake.segments


screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.add_length()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# TODO: 2, move the snake



# TODO: 3, create snake food

# TODO: 4, detect collision with food

# TODO: 5, create a scoreboard

# TODO: 6, detect collision with wall

# TODO: 7, detect collision with tail

screen.exitonclick()
