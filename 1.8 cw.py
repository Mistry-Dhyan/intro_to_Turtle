import turtle
import datetime
##sam = turtle.Turtle()
##sam.setheading(90)
##sam.setheading(180)
##sam.setheading(0)
##sam.setheading(270)

t = turtle.Turtle()
t.penup()
t.goto(0,-180)
t.pendown()
t.circle(180)

t.penup()
t.goto(0,0)
t.setheading(0)
t.forward(150)
t.pendown()
t.forward(30)
t.penup()
t.goto(0,0)

t.penup()
t.right(30)
t.forward(150)
t.pendown()
t.forward(30)
t.penup()
t.goto(0,0)
t.penup()
t.right(30)
t.forward(150)
t.pendown()
t.forward(30)
t.penup()
t.goto(0,0)
t.penup()
t.right(30)
t.forward(150)
t.pendown()
t.forward(30)
t.penup()
t.goto(0,0)
t.penup()
t.right(30)
t.forward(150)
t.pendown()
t.forward(30)
t.penup()
t.goto(0,0)
t.penup()
t.right(30)
t.forward(150)
t.pendown()
t.forward(30)
t.penup()
t.goto(0,0)
t.penup()
t.right(30)
t.forward(150)
t.pendown()
t.forward(30)
t.penup()
t.goto(0,0)
t.penup()
t.right(30)
t.forward(150)
t.pendown()
t.forward(30)
t.penup()
t.goto(0,0)
t.penup()
t.right(30)
t.forward(150)
t.pendown()
t.forward(30)
t.penup()
t.goto(0,0)
t.penup()
t.right(30)
t.forward(150)
t.pendown()
t.forward(30)
t.penup()
t.goto(0,0)
t.penup()
t.right(30)
t.forward(150)
t.pendown()
t.forward(30)
t.penup()
t.goto(0,0)
t.penup()
t.right(30)
t.forward(150)
t.pendown()
t.forward(30)
t.penup()
t.goto(0,0)
t.penup()
t.right(30)
t.forward(150)
t.pendown()
t.forward(30)
t.penup()
t.goto(0,0)

t.penup()
t.goto(0,0)

currentMinute = datetime.datetime.now().minute
currentHour = datetime.datetime.now().hour
t.penup()
t.goto(0,0)
t.color("red")
t.pendown()
t.setheading(90)
t.right(currentHour * 360/12)
t.forward(100)
t.penup()
t.goto(0,0)
t.pendown()
t.setheading(90)
t.right(currentMinute * 360/60)
t.forward(150)
