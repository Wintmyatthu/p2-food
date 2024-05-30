import turtle as r
"""r.title('Smiling Face')
r.speed(10)
r.bgcolor('black')
r.getscreen()
r.pencolor('white')
r.pensize(2)
r.fillcolor('yellow')
r.penup()
r.goto(0,-250)
r.pendown()
r.begin_fill()
r.circle(300)
r.end_fill()

r.fillcolor('white')
r.penup()
r.goto(-150,0)
r.pendown()
r.begin_fill()
r.circle(100)
r.penup()
r.goto(150,0)
r.pendown()
r.circle(100)
r.end_fill()
r.penup()
r.right(90)
r.goto(-100,-100)
r.pendown()
r.circle(100,180)

r.setheading(0)
r.fillcolor('black')
r.penup()
r.goto(-150,50)
r.pendown()
r.begin_fill()
r.circle(50)
r.penup()
r.goto(150,50)
r.pendown()
r.circle(50)
r.end_fill()

r.setheading(-90)
r.fillcolor('white')
r.penup()
r.goto(-50,0)
r.pendown()
r.circle(25,180)
r.setheading(-90)
r.circle(25,180)

r.penup()
r.goto(300,-300)
r.pendown()
r.write('Drawn by Aung Phone Htet',font=("Arial", 19))"""
x=int(input('Input the sides of a polygon'))
y=int(input('Input the lengths of a polygon'))
r.title('Drawing Polygon')
r.speed(10)
r.bgcolor('black')
r.pencolor('blue')
def poly(sides,lengths):
    for i in range(0,sides):
        r.fd(lengths)
        r.rt(360/sides)


poly(x,y)
        


        
    
