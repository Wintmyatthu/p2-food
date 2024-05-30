'''#1. write the python program to display numbers 1 to 5 
i=int(1)
n=int(5)
while i<=n:
    print(i)
    i=i+1'''

#2. Write the program when ur age is greater than 18, Show u can vote.

age=int(input('Enter Age..'))

while age>=18:
    print ('you can vote')
    break
else:
    print('You cannot Vote')

