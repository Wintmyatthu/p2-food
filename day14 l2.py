#3. write a python program to calculate 
# the sum of numbers until the user enters zero.

total= int(0)
num= int(input('Enter the number.  '))

while num!=0:
    total+=num
    num= int(input('Enter the number.  '))
print('The total is ', total)