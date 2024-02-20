# Part 1 ran once and commented out
# import colorgram
import turtle
from turtle import Turtle, Screen
import random

#rgb_tuple_list = []
#colors = colorgram.extract('image.jpg', 30)
#for color in colors:
#    rgb_tuple = (color.rgb[0], color.rgb[1], color.rgb[2])
#    rgb_tuple_list.append(rgb_tuple)

#print(rgb_tuple_list)
color_list = [(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = Turtle()
turtle.colormode(255)
tim.hideturtle()
tim.speed("fastest")
tim.penup()

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
spaces = 50

for j in range(10):
    for i in range(10):
        random_color = random.choice(color_list)
        tim.dot(20,random_color)
        tim.forward(spaces)
    tim.backward(spaces*10)
    tim.setheading(90)
    tim.forward(spaces)
    tim.setheading(0)

screen = Screen()
screen.exitonclick()