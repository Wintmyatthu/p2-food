num1=float(input('Please, enter the first number: '))
num2=float(input('Please, enter the second number: '))

print("""
Choose an operation from the list
1. Addition
2. Subtraction
3. Multiplication
4. Exponentiation
5. Division
6. Division with remainder
""")

choice=int(input('Choice one option: '))

if choice==1:
    print('Sum : {} + {} = {}'.format(num1,num2,num1+num2))
elif choice==2:
    print('Subtract : {} - {} = {}'.format(num1,num2,num1-num2))
elif choice==3:
    print('Multiply : {} * {} = {}'.format(num1,num2,num1*num2))
elif choice==4:
    print('power : {} ^ {} = {}'.format(num1,num2,num1**num2))
elif choice==5: 
    try:
        print('Quotient : {} / {} = {}'.format(num1,num2,num1/num2))
    except:
        print('Division by 0 is not possible!')
elif choice==6:
    try:
        print('Division with remainder : {} / {} = {}. Remainder is {}'.format(num1,num2,num1//num2,num1%num2))
    except:
        print('Division by 0 is not possible!')
else:
    print('Your option is invaild!')
    
    
    