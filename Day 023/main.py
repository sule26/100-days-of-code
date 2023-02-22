import time
from turtle import Screen
from car_manager import CarManager
from scoreboard import Scorebord
from player import Player

Y_MIN = -230
Y_MAX = 230
FINISH_LINE_Y = 280


screen = Screen()
screen.setup(600, 600)
screen.title('Turtle Crossing Game')
screen.tracer(0)

player = Player()
car_manager = CarManager()
scorebord = Scorebord()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect if collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scorebord.game_over()

    # Detect if reached the top
    if player.ycor() > FINISH_LINE_Y:
        player.refresh()
        car_manager.increase_speed()
        scorebord.next_level()

screen.exitonclick()
