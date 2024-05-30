##import turtle as r
##import random
##random.seed()   #random number generator
##r.mode('logo')    #standard, logo, world
##r.speed(10)
##r.title('stamping different shapes')
##r.bgcolor('black')
##r.resizemode('auto')
##colorlist=['red','gold','blue','purple','cyan']
##shapelist=['turtle','square','arrow','circle','triangle','classic']
##def makestamp():
##    r.setheading(random.randint(1,360))
##    r.pensize(random.randint(1,8))
##    r.color(random.choice(colorlist))
##    r.shape(random.choice(shapelist))
##    r.stamp()
##
##r.penup()
##for i in range(15):
##    makestamp()
##    r.setheading(90)
##    r.fd(40)
