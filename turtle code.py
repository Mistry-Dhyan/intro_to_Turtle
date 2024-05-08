import turtle
import random
mr = turtle.Turtle()
while True:
    x = int(input('What is your x input? : '))
    y = int(input('What is your y input? : '))
    a = int(input('How long do you want your polygon? : '))
    q = int(input('How many sides do you want your polygon? : '))
    c = str(input('What color do you want your polygon? : '))
    cf = str(input('What color do you want to color your polygon? : '))
    ps = int(input('How thick do you want your polygon border to be? : '))
    howmanytimes = input('how many times do you want turtle to go? : ')
    ang = 360 / q
    mr.color(c)
    mr.penup()
    mr.fillcolor(cf)
    mr.pensize(ps)
    mr.shape('turtle')
    mr.goto(x,y)
    mr.pendown()
    mr.begin_fill()
    x = random.randint(-250,250)
    y = random.randint(-250,250)
    for i in range(q):
        mr.forward(a)
        mr.left(ang)
    mr.end_fill()
    mr.begin_fill()
    for i in range(howmanytimes):
        mr.goto(x,y)
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        mr.end_fill()
        mr.begin_fill()

