from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("US states game")
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    user_input = screen.textinput(f"{len(guessed_states)}/50 states correct", "What is another state name?").title()
    if user_input == "Exit":
        break
    if user_input in all_states:
        guessed_states.append(user_input)
        x = int(data.x[data["state"] == user_input])
        y = int(data.y[data["state"] == user_input])
        tim = Turtle()
        tim.penup()
        tim.hideturtle()
        tim.goto(x, y)
        tim.write(user_input, align="center", font=('Arial', 8, 'normal'))

states_to_learn = [state for state in all_states if state not in guessed_states]


states_to_learn_data = pandas.DataFrame(states_to_learn)
print(states_to_learn_data)
states_to_learn_data.to_csv("states_to_learn.csv")