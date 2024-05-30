# Given 2 number, write a python code to find the minimum and maximum number.
a= float(input('Enter first number  :'))
b= float(input('Enter second number  :'))

x= min(a,b)
y= max(a,b)

print('The minimum number is',x)
print('The maximum number is',y)

s=a+b
print('The total is ',s )

print('The sum of {0} and {1} is {2}'.format(a,b,s))
