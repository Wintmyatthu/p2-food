import turtle as t
import random
p_one=t.Turtle()
p_one.color('red')
p_one.shape('turtle')
p_one.pu()
p_one.goto(-200,100)
p_one.pd()

p_two=p_one.clone()
p_two.color('blue')
p_two.pu()
p_two.goto(-200,-100)
p_two.pd()

