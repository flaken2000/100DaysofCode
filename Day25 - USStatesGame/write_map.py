from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 10, 'bold')


class WriteMap(Turtle):

    def __init__(self, state, x_coor, y_coor):
        super().__init__()
        self.state = state
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("black")
        self.goto(self.x_coor, self.y_coor)
        self.write(f"{self.state}", align=ALIGNMENT, font=FONT)
