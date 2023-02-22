import turtle
import pandas
import time

FONT = ("Courier", 8, "normal")
IMAGE = "Day 025/blank_states_img.gif"

screen = turtle.Screen()
screen.setup(730, 490)
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)


def create_state(state_name):
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    state_infos = states_data[states_data["state"] == state_name]
    new_turtle.goto(int(state_infos.x), int(state_infos.y))
    new_turtle.write(state_name)


guessed_states = []
score = 0
states_data = pandas.read_csv("Day 025/50_states.csv")
all_states = states_data["state"].to_list()

while score != 50:
    screen.update()
    time.sleep(1)
    answer_state = screen.textinput(
        f"{score}/50 States Correct", "What's another state's name?"
    ).title()

    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Day 025/states_to_learn.csv")
        break
    elif answer_state in all_states:
        create_state(answer_state)
        guessed_states.append(answer_state)
        score += 1


turtle.mainloop()
