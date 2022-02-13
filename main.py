import time
from turtle import Screen, Turtle
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
import math

speed = 0.08
sc = Screen()
sc.title("Pong")
sc.setup(800, 600)
sc.bgcolor((0, 0, 0))
sc.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
sc.listen()
fps = Turtle()
fps.penup()
fps.hideturtle()
fps.goto(0, 220)
fps.color("red")
fps.write(math.floor(1 / speed), align="center", font=("Courier", 30, "normal"))

sc.onkeypress(paddle1.suunta_up, "Up")
sc.onkeypress(paddle1.suunta_down, "Down")
sc.onkeypress(paddle2.suunta_up, "w")
sc.onkeypress(paddle2.suunta_down, "s")
sc.onkeyrelease(paddle1.suunta_empty, "Up")
sc.onkeyrelease(paddle1.suunta_empty, "Down")
sc.onkeyrelease(paddle2.suunta_empty, "w")
sc.onkeyrelease(paddle2.suunta_empty, "s")
game_is_on = True

while game_is_on:
    time.sleep(speed)
    sc.update()
    fps.clear()
    fps.write(math.floor(1 / speed), align="center", font=("Courier", 30, "normal"))
    ball.move()
    paddle1.move()
    paddle2.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.xcor() == 330 and paddle1.ycor() + 51 > ball.ycor() > paddle1.ycor() - 51:
        ball.paddle_bounce()
        speed *= 0.9
        paddle1.speed *= 0.9
    if ball.xcor() == -330 and paddle2.ycor() + 51 > ball.ycor() > paddle2.ycor() - 51:
        ball.paddle_bounce()
        speed *= 0.9
        paddle2.speed *= 0.9
    if ball.xcor() < -400 or ball.xcor() > 400:
        if ball.xcor() > 0:
            scoreboard.l_point()
        else:
            scoreboard.r_point()
        ball.goto(0, 0)
        paddle1.goto(350, 0)
        paddle2.goto(-350, 0)
        sc.update()
        ball.x_move = 10
        ball.y_move = 10
        speed = 0.08
        time.sleep(2)

sc.exitonclick()
