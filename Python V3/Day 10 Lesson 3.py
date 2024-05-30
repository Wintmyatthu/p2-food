is_dark=input('Is it dark outside?(y/n/None)')
if is_dark=='y':
    print('Good night!!')
elif is_dark=='None':
    print('Good Afternoon')
else:  
    print('Good evening!')
    
print('\n')

#a=input('input a:')
#b=input('input b:')
#if a>b:
#    print('a is greater than b')
#else:
#    print('b is greater than a')

#print('\n')

a=input('input a:')
b=input('input b:')
if a>b:
    print('a is greater than b')
elif b==a:
    print('b is the same with a')
else:
    print('b is greater than a')