Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@Biruh-21 
Biruh-21
/
My-python-games
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
My-python-games/SnakeGameGUI/snake.py /
@Biruh-21
Biruh-21 adding SnakeGame to my games
Latest commit 8229783 3 days ago
 History
 1 contributor
54 lines (44 sloc)  1.46 KB

from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            one_sqr = Turtle(shape="square")
            one_sqr.penup()
            one_sqr.color("white")
            one_sqr.setposition(i * -20, 0)
            self.segments.append(one_sqr)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            prev_pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(prev_pos)
        self.head.forward(MOVE_DISTANCE)

    def add_length(self):
        one_sqr = Turtle(shape="square")
        one_sqr.penup()
        one_sqr.color("white")
        last_sqr = self.segments[len(self.segments)-1]
        last_sqr_x = last_sqr.xcor()
        last_sqr_y = last_sqr.ycor()
        one_sqr.setposition(self.segments[-1].position())

        self.segments.append(one_sqr)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
My-python-games/snake.py at main · Biruh-21/My-python-games
