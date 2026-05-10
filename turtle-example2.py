import turtle

a = turtle.Pen()
a.speed('slow')
sides = int(input("how many sides? "))
length = int(input("how long is each side? "))
for x in range(1,sides+1,1):
    a.forward(length)
    a.right(360/sides)

turtle.exitonclick()


