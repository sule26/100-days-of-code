from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.speed(0)
colormode(255)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    tim.color(red, green, blue)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        random_color()
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
