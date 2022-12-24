import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race Game")
screen.bgpic("bgimg.gif")
writer_tim = Turtle()
writer_tim.color("white")
writer_tim.penup()
writer_tim.hideturtle()

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-75, -45, -15, 15, 45, 75]
all_turtle = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color("white", colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_pos[turtle_index])
    all_turtle.append(new_turtle)

is_race_on = False
winner = ''
if user_bet:
    is_race_on = True

while is_race_on:
    for turt in all_turtle:
        if turt.xcor() > 230:
            winner = turt
            is_race_on = False
            break
        rand_len = random.randint(1, 10)
        turt.forward(rand_len)

if user_bet == winner.color()[1]:
    writer_tim.write(f"Congrats you win! The winner is {winner.color()[1]}.", True, align="center", font=('Arial', 12, 'bold'))
else:
    writer_tim.write(f"You lose, The winner is {winner.color()[1]}.", True, align="center", font=('Arial', 12, 'bold'))
screen.exitonclick()