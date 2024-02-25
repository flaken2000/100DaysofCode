from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 16, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("black")
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-240, 260)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
