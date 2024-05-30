import turtle as t
from itertools import cycle

colors = cycle(['red','blue','green','yellow','purple'])

def drawcircle(size,angle,shift):
    t.pencolor(next(colors))
    for i in range(4):
        t.right(angle)
        t.forward(shift)
    drawcircle(size-1, angle+1,shift+1)


t.bgcolor('black')
t.speed(3)
t.pensize(3)
drawcircle(200,0,1)
