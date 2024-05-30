import turtle as t
from random import randint, random

t.Screen().bgcolor('black')
t.title('random ')

def drawstar(points,size,col,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    angle=180-(180/points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()
drawstar( 8,15,'red',50,50)
while True:
    ranpts=randint(2,5)*2 + 1
    ransize=randint(10,60)
    rancol=(random(),random(),random())
    ranx=randint(-350,350)
    rany=randint(-250,250)

    drawstar( ranpts,ransize,rancol,ranx,rany)












##drawstar(7,50,'green',0,0)
