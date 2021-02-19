import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. Stage Game")
image = "blank_states_img.gif"
turtle.tracer(0)
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
score = 0
data = pandas.read_csv("50_states.csv")
data_exit = {"States to learn": []}
data_exit["States to learn"].extend(data.state)
end = False
while not end:
    turtle.update()
    choose = screen.textinput(f"{score}/50 is correct", "What another state name?")
    for state in data.state:
        if choose == state:
            data_exit["States to learn"].remove(state)
            score += 1
            data_state = data[data.state == state]
            pen.goto(int(data_state.x), int(data_state.y))
            pen.write(state, True, "center")
    if score == 50 or choose == "exit":
        end = True
data_list = pandas.DataFrame(data_exit)
data_list.to_csv("state_to_learn.csv")
screen.mainloop()
