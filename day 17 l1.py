#Star

import turtle as t

t.title('Star Shape')
t.bgcolor('black')
t.pencolor('yellow')
t.shape('turtle')
t.pensize(5)

t.speed(1)
for z in range (5):
    t. forward(50)
    t.right(144)


t.penup()
t.setpos(-100,100)
t.pendown()

for z in range (5):
    t. forward(50)
    t.right(144)

t.penup()
t.setpos(100,100)
t.pendown()

for z in range (5):
    t. forward(50)
    t.right(144)
