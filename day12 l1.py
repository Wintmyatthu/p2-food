
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("""
Choose an operation from the list:
1. Addition
2. Subtraction
3. Multiplication
4. Exponentiation
5. Division
6. Division with remainder
""")

op = int(input("Enter the choice number: "))

if op==1:
    print('Sum :{} + {} = {}'.format(a,b,a+b))
elif op==2:
    print('Subtract :{} - {} = {}'.format(a,b,a-b))
elif op==3:
    print('Multiply :{} * {} = {}'.format(a,b,a*b))
elif op==4:
    print('power :{} ^ {} = {}'.format(a,b,a**b))
elif op==5:
    try:
        print('Quotient :{} / {} = {}'.format(a,b,a/b))
    except:
        print('Division by 0 is not possible')
elif op==6:
    try:
        print('Division with remainder: {} / {} = {}. Remainder is {}'.format(a,b,a//b,a%b))
    except:
        print('Division by 0 is not possible')
else:
    print('option is invilid')