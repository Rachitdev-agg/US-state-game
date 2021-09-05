import turtle
import pandas

score = 0
guessed = []
states_left = []
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50", prompt="What's another state's name?").title()
    if answer_state in guessed:
        pass
    else:
        for n in data["state"]:
            if answer_state == "Exit":
                states_left = [state for state in data["state"] if state not in guessed]
                game_is_on = False
            if answer_state == n:
                guessed.append(answer_state)
                score += 1
                coor = data[data["state"] == answer_state]
                correct_state = turtle.Turtle()
                correct_state.hideturtle()
                correct_state.penup()
                correct_state.goto(int(coor.x), int(coor.y))
                correct_state.write(f"{answer_state}", align="center", font=("Courier", 10, "normal"))

new_data = pandas.DataFrame(states_left)
new_data.to_csv("states_to_learn.csv")