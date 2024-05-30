import turtle as c
d=['red','green','blue']
for i in range(4):
    c.fillcolor(d[i%3])
    c.begin_fill()
    c.circle(90)
    c.rt(90)
    c.end_fill()
