from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):

        # Create snakes
        self.timmys = []
        self.create_snake()
        self.head = self.timmys[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self,position):
        new_timmy = Turtle(shape="square")
        new_timmy.color("white")
        new_timmy.penup()
        new_timmy.speed("fastest")
        new_timmy.goto(position)
        self.timmys.append(new_timmy)

    def extend(self):
        self.add_segment(self.timmys[-1].position())

    def move(self):
        for timmy in range(len(self.timmys) - 1, 0, -1):
            new_x = self.timmys[timmy - 1].xcor()
            new_y = self.timmys[timmy - 1].ycor()
            self.timmys[timmy].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for segment in self.timmys:
            segment.goto(1000,1000)
        self.timmys.clear()
        self.create_snake()
        self.head = self.timmys[0]