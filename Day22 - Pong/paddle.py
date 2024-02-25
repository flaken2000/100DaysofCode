from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.x_pos = x_pos
        self.penup()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(10, 1)
        self.goto(self.x_pos, 0)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 30)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 30)
