import turtle as r
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
        r.stamp()
