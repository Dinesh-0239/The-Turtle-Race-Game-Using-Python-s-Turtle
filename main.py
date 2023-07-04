#Importing Necessary Modules
from turtle import Turtle, Screen, title, textinput
from random import randint

#create title for the app
title("The Turtle Race")
#Turtle participants colors
turtle_colors = ["violet","indigo","blue","green","yellow","orange","red"]
#empty list to hold turtle objects
turtles = []
#initializing Screen object for race track
race_track = Screen()
race_track.bgcolor("black") #setup background color for race track
race_track.setup(width=600,height=400) #setup dimentions for race track
race_track._root.iconbitmap("AppIcon.ico")
race_track.cv._rootwindow.resizable(False, False) #restrict race track to expand or shrink
is_race_end = 0 #boolean variable for figure out wheter the race is continue or end
y_axis = -150 #initilising y-axis to place participants
def setup_turtles(turtle):
    """Setup turtle participants in their respective position"""
    global y_axis
    turtle.goto(x=-270,y=y_axis)
    y_axis += 50

#Creating turtle object and append them into turtle list and also give them colors and shape
for turtle_index in range(7):
    turtles.append(Turtle(shape="turtle"))
    turtles[turtle_index].penup()
    turtles[turtle_index].color(turtle_colors[turtle_index])
    setup_turtles(turtles[turtle_index])

#Ask for bid on one turtle
user_bid = textinput("User Bid",f"Bid on one turtle from {turtle_colors} will going to win: ").lower()
#show the user bid during the race
turtles[turtle_colors.index(user_bid)].shapesize(1.5)


#logic for conducting race
while not is_race_end:
    for turtle in turtles:
        #checking turtles they have reach the finish line or not
        if turtle.xcor() > 280:
            t = Turtle() #Create one more turtle object to show win or lost message
            t.hideturtle() #Hide the msg turtle
            winner = turtle.color() #Extract color tuple of winner turtle
            t.color(winner[0]) #give the winner color to the msg turtle
            #checking winner and user bid is the same or not
            if winner[0] == user_bid:
                msg = f"You win! The {winner[0].upper()} wins the race.\t"
            else:
                msg = f"You lost! The {winner[0].upper()} wins the race.\t"
            t.write(msg,align="center",font = ("Arial",18,"bold")) #display the result
            is_race_end = True #end the race

    turtles[randint(0,6)].forward(randint(1,10)) #moves the turtles

race_track.exitonclick()