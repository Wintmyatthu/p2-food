"""import turtle as r
from itertools import cycle

colors=cycle(['red','blue','cyan','gold','yellow','green','purple'])

def drawcircle(size,angle,shift):
    r.pencolor(next(colors))
    r.circle(size)
    r.rt(angle)
    r.fd(shift)
    drawcircle(size-100,angle-1,shift-1)
    

r.bgcolor('black')
r.speed(10)
r.pensize(3)
drawcircle(300,0,1)"""



import turtle as car
car = car.Turtle()
car.pencolor('silver')
car.color('red')
car.fillcolor('black')
car.penup()
car.goto(-50, 0)
car.pendown()
car.begin_fill()
car.forward(100)
car.left(90)
car.forward(20)
car.left(90)
car.forward(100)
car.left(90)
car.forward(20)
car.end_fill()

car.penup()
car.goto(-30, -20)
car.pendown()
car.color('black')
car.fillcolor('black')
car.begin_fill()
car.circle(20)
car.end_fill()
car.penup()
car.goto(30, -20)
car.pendown()
car.begin_fill()
car.circle(20)
car.end_fill()

car.hideturtle()

turtle.exitonclick()




