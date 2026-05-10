import turtle


t = turtle.Pen()
t.speed('fast')
x = 10


for s in range(1,10,1):
    for i in range(1, x+1):
        t.forward(s)
        t.right(360/x)



turtle.exitonclick()


a = turtle.Pen()
a.speed('slow')
sides = int(input("how many sides? "))
length = int(input("how long is each side? "))
for x in range(1,sides+1,1):
    a.forward(length)
    a.right(360/sides)
