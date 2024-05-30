import turtle
s=turtle.Screen()
s.setup(1000,600)
s.title('Ping Pong Paradise')
s.bgcolor('black')

#left paddle
l=turtle.Turtle()
l.shape('square')
l.color('white','blue')
l.shapesize(6,2)
l.penup()
l.goto(400,0)

#right paddle
r=turtle.Turtle()
r.shape('square')
r.color('white','red')
r.shapesize(6,2)
r.penup()
r.goto(-400,0)

#Ball
b=turtle.Turtle()
b.shape('circle')
b.color('white')
b.penup()
b.goto(0,0)
b.dx=5
b.dy=-5

#initialize
r_p=0
l_p=0

#display score
sc=turtle.Turtle()
sc.hideturtle()
sc.color('white')
sc.pu()
sc.goto(0,250)
sc.write('Right Player: 0                             Left player: 0',align='center', font=("Verdana",25, "bold"))

#Movement funtion
def R_U():
    y=r.ycor()
    y+=10
    r.sety(y)

def R_D():
    y=r.ycor()
    y-=10
    r.sety(y)


#Keys
s.listen()
s.onkeypress(R_D,'s')

s.listen()
s.onkeypress(R_U,'w')

def L_U():
    y=l.ycor()
    y+=10
    l.sety(y)

def L_D():
    y=l.ycor()
    y-=10
    l.sety(y)


#Keys
s.listen()
s.onkeypress(L_D,'Down')

s.listen()
s.onkeypress(L_U,'Up')

#Start game
while True:
    s.update()
    b.setx(b.xcor()+b.dx)
    b.sety(b.ycor()+b.dy)

#check ball
    if b.ycor()<-280:
        b.sety(-280)
        b.dy*=-1

    if b.ycor()>280:
        b.sety(280)
        b.dy*=-1

    if b.xcor()<-480:
        b.goto(0,0)
        b.dy*=-1
        l_p+=1
        sc.clear()
        sc.write('Right Player: {}                             Left player: {}'.format(r_p,l_p),align='center', font=("bitmap",25, "bold"))

    if b.xcor()>480:
        b.goto(0,0)
        b.dy*=-1
        r_p+=1
        sc.clear()
        sc.write('Right Player: {}                             Left player: {}'.format(r_p,l_p),align='center', font=("bitmap",25, "bold"))

#collision ball & paddle
        if ((b.xcor()>370 and b.xcor()<380) and (b.ycor()<l.b.ycor()+80 and b.ycor()>l.ycor-80)):
            b.setx(370)
            b.dx*=-1

        if ((b.xcor()<-370 and b.xcor()>-380) and (b.ycor()<r.b.ycor()+80 and b.ycor()>r.ycor-80)):
            b.setx(-370)
            b.dx*=-1
