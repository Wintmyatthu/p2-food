# 1. Ask the user for a number. depending on whether the number is even or odd,
# write a python code to print out an appropriate msg to the user.


#2. write the python program to print the maximum of three integers entered by the user.
    
x = int ( input ("Please enter an integer:"))
y = int ( input ("Please enter another integer:"))
z = int ( input ("Please enter a third integer:"))

if x>y>z:
    print('The largest number is ',x)
elif y>x>z:
    print('The largest number is ',y)
else:
    print('The largest number is ',z)
    
#3. Consider writing the python code where we want the user to enter 2 floats and then
# choose one option to add,sub,mul,div.and calculate and show the answer.

x= float(input('Enter x  '))
y= float(input('Enter y  '))

print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Division')

choice= (input('Please enter your choice  '))

if choice=='1':
    print('The addition is',x+y)
elif choice=='2':
    print('The subtraction is',x-y)
elif choice=='3':
    print('The multiplication is',x*y)
elif choice=='4':
    print('The division is',x/y)
else: print ('Input is invalid')




