import turtle 
import pandas

screen = turtle.Screen()
screen.title("U.S states Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
cursor = turtle.Turtle()
cursor.hideturtle()
cursor.penup()
cursor.speed("fastest")

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
cor_st = []

rep = 0
while rep <= 50:
    answer_state = screen.textinput(title=f"{rep}/50 States Correct",prompt="Type another name's state:").title()

    if answer_state in states :
        cor_st.append(answer_state)
        st = data[data.state == answer_state]
        x = int(st.x)
        y = int(st.y)
        cursor.goto(x,y)
        cursor.write(answer_state)
        rep +=1 

    elif answer_state == "Exit":
        abs_st = [st for st in states if st not in cor_st]
        pandas.DataFrame(abs_st).to_csv("absent_states.csv")
        break

