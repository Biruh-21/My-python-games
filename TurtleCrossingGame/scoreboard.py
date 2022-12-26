from turtle import Turtle
FONT = ("Courier", 24, "bold")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self, start):
        super().__init__()
        self.start = start
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-230, 260)
        if self.start:
            self.next_level()
        print("created")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def next_level(self):
        self.clear()
        self.write(f"Level {self.level}", align=ALIGNMENT, font=("Courier", 16, "bold"))
