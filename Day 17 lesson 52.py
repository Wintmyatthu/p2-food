import turtle as h
c=['red','green','blue','gray','orange']
h.pensize(5)
for a in range(6):
    h.pencolor(c[a%5])
    h.fd(100)
    h.lt(60)
