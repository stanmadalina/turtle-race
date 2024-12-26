import random
from random import choice
from turtle import Turtle, Screen
colors = ["red", "orange", "blue", "yellow", "green", "purple"]
race = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bets!", prompt=f"Which turtle will win? Enter a color: {colors}")
tim_list = []
if bet:
    race = True

x = -230
y = -90
for i in range(0, 6):
    new_tim = Turtle(shape="turtle")
    new_tim.color(colors[i])
    new_tim.penup()
    new_tim.goto(x, y)
    tim_list.append(new_tim)
    y += 30

while race:
    for tim in tim_list:
        if tim.xcor() > 230:
            race = False
            winner = tim.pencolor()
            if winner == bet:
                print("You won!")
            else:
                print("you lost!")
        dist = random.randint(0, 10)
        tim.forward(dist)










screen.exitonclick()
