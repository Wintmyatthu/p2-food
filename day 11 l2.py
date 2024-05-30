#3. Consider writing the python code where we want the user to enter 2 floats and then
# choose one option to add,sub,mul,div.and calculate and show the answer.

num1=float(input('num1='))
num2=float(input('num2='))
choice=str(input('Enter an operator'))

if choice=='+': 
    print(num1+num2)
elif choice=='-':
    print(num1-num2)
elif choice=='*':
    print(num1*num2)
elif choice=='/':
    print(num1/num2)
else:
    print ('Input is invilid')

