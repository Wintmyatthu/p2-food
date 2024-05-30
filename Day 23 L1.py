import turtle as t
import random
tnum=random.randint(1,10)
t.setup(500,500)

t.speed(10)

t.shape("turtle")     # Select turtle's shape.
t.color("blue")
t.penup()
t.goto(-200, 100)       # Set turtle's starting position.


#clone
snum=random.randint(1,10)
s=t.clone()
s.color("red")
s.penup()
s.goto(-200,-100)

#goal
t.goto(300,60)
t.pd()
t.circle(40)
t.pu()
t.goto(-200,100)
s.goto(300,-140)
s.pd()
s.circle(40)
s.pu()
s.goto(-200,-100)



while True:
    t.fd(tnum)
    s.fd(snum)
    if t.pos()>=(300,100):
        print('Player one Win!')
        break
    elif s.pos()>=(300,-100):
        print('Player two Win!')
        break
