from scorebord import Scorebord
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

LEFT_POSITION = (-350, 0)
RIGHT_POSITION = (350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(LEFT_POSITION)
r_paddle = Paddle(RIGHT_POSITION)
ball = Ball()
scorebord = Scorebord()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(l_paddle) < 50 and ball.xcor() > -320 or ball.distance(r_paddle) <= 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        scorebord.l_point()
        ball.reset_position()

    # Detect L paddle misses
    if ball.xcor() < -380:
        scorebord.r_point()
        ball.reset_position()

screen.exitonclick()
