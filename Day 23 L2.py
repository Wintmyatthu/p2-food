import turtle as t
def cake():
    t.circle(50)
    t.circle(150)

def tri():
    for i in range(3):
        t.fd(100)
        t.rt(120)
t.listen()
t.onkey(cake,'space')
t.onkey(tri,'Up')
##t.onkeypress(fun,key)
##t.onkey(fun,key)
