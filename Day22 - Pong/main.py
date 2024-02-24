from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game 3000")
screen.tracer(0)

right_paddle = Paddle(x_pos=350)
left_paddle = Paddle(x_pos=-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
game_speed_start = 0.1
game_speed = game_speed_start
while game_is_on:
    time.sleep(game_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detect collision with paddles
    if ball.distance(right_paddle) < 60 and ball.xcor() > 320 or ball.distance(left_paddle) < 60 and ball.xcor() < - 320:
        ball.paddle_bounce()
        game_speed *= 0.8

    # Detect when ball goes out of bounds
    # Right paddle
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.addpoint("l")
        game_speed = game_speed_start

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.addpoint("r")
        game_speed = game_speed_start


screen.exitonclick()
