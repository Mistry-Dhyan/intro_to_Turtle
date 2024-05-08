import turtle
from random import randint # this is how we get random numbers
screen=turtle.Screen() # create a screen object called 'screen'
screen.bgcolor('black') # set the background colour to black
me = turtle.Turtle()# create a turtle named 'me' this will be the turtle you control
me.color('cyan')# set the turtle's colour to your favourite colour
dot = turtle.Turtle()# create a new turtle named 'dot', they will draw the stars
dot.speed(0)# set dot's speed to 0
dot.penup()# dot needs to lift their pen
dot.hideturtle()# dot needs to be invisible
dot.color('white')# set dot's colour to white
screen.onclick(me.goto)
for i in range(20): # change '20' to a bigger number for more stars!
    dot.goto(randint(-200,200), randint(-200,200)) #random place
    dot.begin_fill()
    dot.circle(randint(3,10)) #dot draws a circle of random size
    dot.end_fill() # the circle is filled in!
