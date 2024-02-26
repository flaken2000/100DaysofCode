from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.score = 0
        self.get_high_score()
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def addpoint(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        self.update_high_score()
        self.score = 0
        self.get_high_score()
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())

    def update_high_score(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
