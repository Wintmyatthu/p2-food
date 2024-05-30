import turtle as r
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
drawcircle(300,0,1)
