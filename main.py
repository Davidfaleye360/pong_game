from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(800, 600, 'black')
screen.title('Pong')
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.move_up, 'Up')
screen.onkeypress(right_paddle.move_down, 'Down')
screen.onkeypress(left_paddle.move_up, 'w')
screen.onkeypress(left_paddle.move_down, 's')
sleep_time = 0.1


game_on = True
while game_on:
    time.sleep(sleep_time)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 60 and ball.xcor() > 320 or ball.distance(left_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()
        if sleep_time >= 0.01:
            sleep_time -= 0.01

    if ball.xcor() > 330:
        ball.restart()
        scoreboard.l_point()
        sleep_time = 0.1

    elif ball.xcor() < -330:
        ball.restart()
        scoreboard.r_point()
        sleep_time = 0.1


screen.exitonclick()
