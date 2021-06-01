
import pandas
from turtle import Turtle, Screen
image = "blank_states_img.gif"

screen_obj = Screen()
turtle_obj = Turtle()

screen_obj.title("US States Game!")
screen_obj.addshape(image)
turtle_obj.shape(image)

# import turtle
# def get_mouse_click_co_or(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_co_or)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
# print(all_states)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen_obj.textinput(title="{0}/50 states".format(len(guessed_states)),
                                        prompt="What's another states name?").title()
    # print(answer_state)
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# screen_obj.exitonclick()
