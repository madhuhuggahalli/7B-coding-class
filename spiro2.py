import turtle

painter = turtle.Turtle()

painter.penup()
painter.goto(0,0)
painter.pendown()

painter.pencolor("gold")
for i in range(10,100):
    painter.forward(i*3)
    painter.left(111) # Let's go counterclockwise this time

painter.penup()
painter.hideturtle()
painter.goto(0,0)
painter.pendown()


painter.pencolor("violet")
for i in range(10,100):
    painter.forward(i*3)
    painter.left(107) # Let's go counterclockwise this time

painter.penup()
painter.hideturtle()
painter.goto(0,0)
painter.pendown()

painter.pencolor("magenta")
for i in range(10,100):
    painter.forward(i*3)
    painter.left(113) # Let's go counterclockwise this time

painter.penup()
painter.hideturtle()
painter.goto(0,0)
painter.pendown()

painter.pencolor("green")
for i in range(10,100):
    painter.forward(i*3)
    painter.left(111) # Let's go counterclockwise this time

painter.penup()
painter.hideturtle()
painter.goto(0,0)
painter.pendown()

painter.pencolor("blue")
for i in range(10,100):
    painter.forward(i*3)
    painter.left(115) # Let's go counterclockwise this time

painter.penup()
painter.hideturtle()
painter.goto(0,0)
painter.pendown()

painter.pencolor("green")
for i in range(10,100):
    painter.forward(i*3)
    painter.left(99)

turtle.done()

