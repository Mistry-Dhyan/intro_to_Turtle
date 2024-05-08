import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(1000,1000)

a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
Dhyan = turtle.Turtle()

Dhyan.speed(0)
a.speed(10)
b.speed(20)
c.speed(30)
d.speed(40)

a.shape("turtle")
b.shape("turtle")
c.shape("turtle")
d.shape("turtle")
Dhyan.shape('turtle')

a.color("blue")
b.color("purple")
c.color("grey")
d.color("red")
Dhyan.color('cyan')

a.penup()
b.penup()
c.penup()
d.penup()
Dhyan.penup()

a.goto(110,110)
b.goto(210,-120)
c.goto(-330,130)
d.goto(440,140)
Dhyan.goto(450,150)
screen.bgcolor("pink")

a.right(160)
b.right(260)
c.right(360)
d.right(460)
Dhyan.right(560)
screen.bgcolor("light blue")
a.left(1120)
b.left(2120)
c.left(3120)
d.left(4120)
Dhyan.left(5120)
screen.bgcolor("yellow")

screen.onclick(Dhyan.goto)

