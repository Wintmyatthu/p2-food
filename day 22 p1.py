import turtle as t
import random
t.title('Day 22 project')
t.bgcolor('blue')
t.shape('turtle')
t.pu()
t.colormode(255)
paces=0
randomred=250
randomgreen=250
randomblue=250
for a in range(50):
    t.pu()
    t.goto(0,0)
    paces=2
    for i in range(100):
        randomred=random.randint(0,255)
        randomgreen=random.randint(0,255)
        randomblue=random.randint(0,255)
        t.color(randomred,randomgreen,randomblue)
        paces+=1.5
        t.fd(paces)
        t.right(69)
        t.stamp()

