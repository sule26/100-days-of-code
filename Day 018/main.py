from turtle import Turtle, Screen, colormode
import random

color_list = [
    (211, 154, 98),
    (53, 107, 131),
    (242, 178, 246),
    (120, 20, 244),
    (177, 78, 33),
    (198, 142, 35),
    (116, 155, 171),
    (124, 79, 98),
    (123, 175, 157),
    (226, 197, 130),
    (190, 88, 109),
    (12, 50, 64),
    (56, 39, 19),
    (41, 168, 128),
    (50, 126, 121),
    (199, 123, 143),
    (166, 21, 30),
    (224, 93, 79),
    (243, 163, 161),
    (38, 32, 34),
    (3, 25, 25),
    (80, 147, 169),
    (161, 26, 22),
    (21, 78, 90),
    (234, 167, 171),
    (171, 206, 190),
    (103, 127, 156),
    (165, 202, 210),
    (61, 60, 72),
    (183, 190, 204),
    (78, 66, 42),
    (23, 99, 96),
]

colormode(255)
tim = Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()
STANDARDX = -200
STANDARDY = -200
tim.setposition(STANDARDX, STANDARDY)
number_of_dots = 100


def draw_circles():
    tim.dot(20, random.choice(color_list))


for dot_count in range(1, number_of_dots + 1):
    draw_circles()
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.sety(tim.ycor() + 50)
        tim.setx(STANDARDX)


screen = Screen()
screen.exitonclick()
