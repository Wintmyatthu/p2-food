##import turtle as r
##r.bgcolor('black')
##r.shape('turtle')
##r.color('cyan')
##r.penup()
##r.goto(-150,0)
##for i in range(4):
##    r.penup()
##    r.stamp()
##    r.forward(150)
##    r.left(90)
##r.pendown()
##    
##import turtle as r
##r.penup()
##r.goto(40,0)
##r.pendown()
##r.bgcolor('black')
##r.color('cyan')
##r.shape('turtle')
##for i in range(5):
##    r.fd(100)
##    r.rt(144)
##    r.stamp()

"""import turtle as r
import random
r.title('Stamp turtle graphic')
r.bgcolor('khaki')
r.shape('turtle')
r.penup()
r.colormode(255)
paces=0
randomred=250
randomgreen=250
randomblue=250
for I in range(50):
    r.penup()
    r.goto(0,0)
    paces=2
    for i in range(100):
        randomred=random.randint(0,255)
        randomgreen=random.randint(0,255)
        randomblue=random.randint(0,255)
        r.color(randomred,randomgreen,randomblue)
        paces+=1.5
        r.forward(paces)
        r.right(68+1)
        r.stamp()"""

import turtle as r
r.title('challange')
r.bgcolor('black')
p=['blue','red','gold','cyan','yellow','green']
r.pensize(5)
r.penup()
r.goto(-500,0)
r.pendown()
for I in range(20):
    r.fd(30)
    for i in range(5):
        r.pencolor(p[i%6])
        r.fd(50)
        r.rt(144)
        


    


