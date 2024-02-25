from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("yellow")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def addpoint(self, player):
        if player == "l":
            self.l_score += 1
        else:
            self.r_score += 1
        self.update_scoreboard()

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

