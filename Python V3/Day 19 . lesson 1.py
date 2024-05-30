import turtle as r
"""r. title('The letter A ')
r.pensize(4)
r.bgcolor('black')
r.pencolor('cyan')
r.lt(70)
r.fd(100)
r.rt(140)
r.fd(100)
r.back(50)
r.setheading(180)
r.fd(30)

r.penup()
r.goto(75,50)
r.pendown()
r.setheading(270)
r.fd(50)
r.setheading(0)
r.fd(30)
r.setheading(90)
r.fd(50)
r.penup()

r.goto(120,0)
r.pendown()
r.setheading(90)
r.fd(50)
r.setheading(0)
r.fd(30)
r.setheading(270)
r.fd(50)

r.penup()
r.goto(190,0)
r.pendown()
r.setheading(0)
r.circle(20)
r.penup()
r.goto(210,20)
r.pendown()
r.setheading(270)
r.fd(50)
r.setheading(180)
r.fd(30)

r.write(' Phone Htet')"""

from random import randint, random
put=input('You do not need to write anything here')
r.title('random spawing stars')
r.bgpic('C:\Users\HP\Downloads\sunset-8120.gif')
def drawstar(point,size,col,x,y):
    r.penup()
    r.goto(x,y)
    r.pendown()
    r.bgcolor('black')
    r.color(col)
    r.begin_fill()
    angle=180-(180/point)
    for i in range(point):
        r.fd(size)
        r.rt(angle)
    r.end_fill()

if put=='':
    while True:
        ranpts=randint(2,5)*2+1
        ransize=randint(10,35)
        rancol=(random(),random(),random(),)
        ranx=randint(-300,300)
        rany=randint(-270,270)
        drawstar(ranpts,ransize,rancol,ranx,rany)
else:
    turtle.Terminator()
