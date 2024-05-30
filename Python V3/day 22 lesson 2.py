import turtle as t
t.bgcolor('grey')
t.shape('turtle')
t.color('blue')
t.pu()
t.goto(-200,100)

#clone
s=t.clone()
s.color('white')
s.goto(-200,-100)

r=s.clone()
r.setheading(180)
r.color('black')
r.goto(200,100)

R=r.clone()
r.setheading(180)
R.color('cyan')
R.goto(200,-100)
