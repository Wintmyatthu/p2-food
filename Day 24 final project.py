import turtle
#screen
s=turtle.Screen()
s.setup(1000,600)
s.title('P_P game')
s.bgcolor('black')

#Left paddle
l=turtle.Turtle()
l.shape('square')
l.color('white','red')
l.shapesize(6,2)
l.penup()
l.goto(400,0)

#Right paddle
r=turtle.Turtle()
r.shape('square')
r.color('white','blue')
r.shapesize(6,2)
r.penup()
r.goto(-400,0)

#Ball
b=turtle.Turtle()
b.shape('circle')
b.color('yellow','white')
b.penup()
b.goto(0,0)
b.dx=5
b.dy=-5

#initialize
r_p=0
l_p=0

#display score
sc=turtle.Turtle()
sc.ht()
sc.color('red')
sc.pu()
sc.goto(0,200)
sc.write("Right Player: 0            Left Player:0",align='center',font=('Arial',24,'normal'))



#moving fun
def p_l_u():
    y=l.ycor()
    y+=20   #y=y+20
    l.sety(y)
def p_l_d():
    y=l.ycor()
    y-=20   #y=y+20
    l.sety(y)
def p_r_u():
    y=r.ycor()
    y+=20   #y=y+20
    r.sety(y)
def p_r_d():
    y=r.ycor()
    y-=20   #y=y+20
    r.sety(y)
    
#keys    
s.listen()
s.onkey(p_l_u,'Up')
s.onkey(p_l_d,'Down')
s.onkey(p_r_u,'a')
s.onkey(p_r_d,'s')

#game play
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

    if b.xcor()<-500:
        b.goto(0,0)
        b.dy*=-1
        l_p+=1
        sc.clear()
        sc.write("Right Player:{}            Left Player:{}".format(r_p,l_p),align='center',font=('Arial',24,'normal'))

    if b.xcor()>500:
        b.goto(0,0)
        b.dy*=-1
        r_p+=1
        sc.clear()
        sc.write("Right Player:{}            Left Player:{}".format(r_p,l_p),align='center',font=('Arial',24,'normal'))    

#collision ball & paddle
    if ((b.xcor()>370 and b.xcor()<380) and (b.ycor() < l.ycor()+80 and b.ycor() > l.ycor()-80)):
        b.setx(370)
        b.dx*=-1

    if ((b.xcor()<-370 and b.xcor()>-380) and (b.ycor()< r.ycor()+80 and b.ycor()> r.ycor()-80)):
        b.setx(-370)
        b.dx*=-1
