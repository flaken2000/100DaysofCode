import turtle
import pandas
from write_map import WriteMap

screen = turtle.Screen()
screen.title("U.S. States Game 3000")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

game_is_on = True

correct_guesses = []
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state").title()
    if answer_state == "Exit":
        break
    # Find if answer_state is present in csv
    x = data[data["state"] == answer_state]
    if answer_state in all_states:
        # Get coordinates
        # Pull the row
        state_data = data[data.state == answer_state]
        write_map = WriteMap(answer_state, int(state_data.x), int(state_data.y))
        correct_guesses.append(answer_state)



