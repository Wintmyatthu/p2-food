##num1=int(input('Enter a num1'))
##num2=int(input('Enter a num2'))
##def add(num1,num2):
##    add=num1+num2
##    print(add)
##def sub(num1,num2):
##    sub=num1-num2
##    print(sub)
##
##add(num1,num2)
##sub(num1,num2)
import turtle as e
e.write("Draw By M & A",font=(1000))
def circle():
    e.circle(100)
circle()

def rec():
    e.penup()
    e.goto(200,200)
    e.pendown()
    e.fillcolor('red')
    e.begin_fill()
    for i in range(2):
        e.fd(50)
        e.rt(90)
        e.fd(25)
        e.rt(90)
    e.end_fill()
rec()

    
