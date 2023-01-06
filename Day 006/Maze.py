""" def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif not wall_in_front():
        move()
    else:
        turn_left()
         """
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
 # https://reeborg.ca/reeborg.html      Map: Maze
