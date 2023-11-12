import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S States Game")
image= "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
    
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pd.read_csv("50_states.csv")
all_states = data.state.tolist()
guess_state = []

while len(guess_state) < 50:
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 States Correct", prompt="What's another state's name? ").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guess_state]
        print(missing_states)
        df = pd.DataFrame(missing_states)
        df.to_csv("missing_states.csv")
        break
    if answer_state in all_states:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
