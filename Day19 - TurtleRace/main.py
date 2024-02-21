from turtle import Turtle, Screen
import random

# input pick a color to win

# 6 turtles, red, orange, yellow, green, blue, purple
# set positions
# random steps forwards
# first turtle to cross the screen wins
# at the end, message the user you win/you lose. The XX turtle is the winner.

is_race_on = False

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
timmys = {}
y_position = -130

for color in colors:
    timmy = f"{color}"
    timmys[timmy] = Turtle(shape="turtle")
    timmys[timmy].color(color)
    timmys[timmy].penup()
    timmys[timmy].goto(x=-220, y=y_position)
    y_position += 50

if user_bet:
    is_race_on = True

while is_race_on:
#for x in range(20):
    for color in colors:
        random_distance = random.randint(0,10)
        timmys[color].forward(random_distance)
        if round(timmys[color].xcor()) > 230:
            is_race_on = False
            if user_bet == color:
                print(f"You got it! The {color} turtle is the winner.")
            else:
                print(f"Too bad. The {color} turtle is the winner.")

screen.exitonclick()






