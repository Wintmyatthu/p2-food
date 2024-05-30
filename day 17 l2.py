import turtle as t

t.title('Star Shape')
t.bgcolor('black')

cor=['red','cyan','dimgray','gold','honeydew']
t.shape('turtle')
t.pensize(4)

t.penup()
t.setpos(-100,100)
t.pendown()

t.speed(1)

for i in range (5):
    t.pencolor(cor[i])
    t. forward(100)
    t.right(144)
