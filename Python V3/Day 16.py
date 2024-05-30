import turtle as r

def circle():
    r.pencolor('blue')
    r.bgcolor('black')
    r.penup()
    r.goto(-490,150)
    r.pendown()
    r.circle(100)

circle()

def rec():
    r.pencolor('blue')
    r.penup()
    r.goto(-350,150)
    r.pendown()
    for y in range(2):
        r.fd(90)
        r.rt(90)
        r.fd(40)
        r.rt(90)
r.lt(90)
rec()

triangle=(90**2+90**2)**0.5

def tri():
    for i in range(1):
            r.penup()
            r.goto(-210,150)
            r.pendown()
            r.pencolor('blue')
            for I in range(2):
                          r.forward(90)
                          r.left(90)
    r.left(45)
    H=(90**2+90**2)**0.5
    r.forward(H)
tri()

def squ():
    r.pencolor('blue')
    r.penup()
    r.goto(-150,200)
    r.pendown()
    for y in range(2):
        r.fd(90)
        r.rt(90)
        r.fd(90)
        r.rt(90)
r.lt(90)
squ()

def hex():
        r.pencolor('blue')
        r.penup()
        r.goto(10,150)
        r.pendown()
        for i in range(0,6):
            r.forward(70)
            r.left(60)
r.right(60)
hex()

def pan():
        r.pencolor('blue')
        r.penup()
        r.goto(170,250)
        r.pendown()
        for i in range(0,5):
            r.forward(100)
            r.left(72)
r.right(72)
pan()

angle=360/12
def poly():
        r.pencolor('blue')
        r.penup()
        r.goto(360,270)
        r.pendown()
        for i in range(0,12):
            r.forward(55)
            r.lt(angle)
r.rt(angle)
poly()

angle=360/8
def sep():
        r.pencolor('blue')
        r.penup()
        r.goto(-300,-30)
        r.pendown()
        for i in range(8):
            r.forward(50)
            r.rt(angle)
r.lt(angle)
sep()

angle=360/9
def non():
        r.pencolor('blue')
        r.penup()
        r.goto(-490,-20)
        r.pendown()
        for i in range(9):
            r.forward(50)
            r.rt(angle)
r.lt(angle)
non()
    
        

    
        
    

r.pencolor('blue')
r.pensize(5)
r.penup()
r.goto(200,-100)
r.pendown()
r.write('Drawn by Aung Phone Htet',font=("Arial", 19))



