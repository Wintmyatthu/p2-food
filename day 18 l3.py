import turtle as t

def drawpolygon(sides,length):
    for i in range(0,sides):
        t.forward(length)
        t.right(360/sides)

drawpolygon(10,100)
