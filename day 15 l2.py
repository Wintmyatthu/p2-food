##right triangle

o=input('Enter opposite side')
a=input('Enter adjcent side')
import turtle as t


t.forward(float(o))
t.left(90)
t.forward(float(a))
t.left(135)
h=((float(o)**2)+(float(a)**2))**0.5
t.forward(h)
