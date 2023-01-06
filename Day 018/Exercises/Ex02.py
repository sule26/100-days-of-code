from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.speed(0)
tim.pensize(15)
colormode(255)
directions = [0, 90, 180, 270]


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    tim.color(red, green, blue)


def random_move():
    angle = random.choice(directions)
    tim.setheading(angle)
    tim.forward(20)


for i in range(1000):
    random_color()
    random_move()


screen = Screen()
screen.exitonclick()
