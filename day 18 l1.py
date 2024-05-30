import turtle as t
t.getscreen()
t.speed(1)
t.pensize(8)
t.pencolor("red")

t.fillcolor('yellow')
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(-50,150)
t.pendown()
t.fillcolor('yellow')
t.begin_fill()
t.circle(100,180)
t.end_fill()

t.penup()
t.goto(-50,-150)
t.pendown()
t.fillcolor('yellow')
t.begin_fill()
t.circle(100,270)
t.end_fill()

t.penup()
t.goto(-150,-200)
t.setheading(270)
t.pendown()

