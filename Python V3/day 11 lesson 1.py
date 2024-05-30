#num=int(input('Please, input the first number:'))
#num2=int(input('Please, input the second number:'))
#num3=int(input('Please, input the third number:'))

#if num>num2>num3:
 #   print(num,' is the largest.')
#elif num2>num>num3:
  #  print(num2,'is the largest.')
#else:
 #   print(num3,'is the largest.')









#if ((num%2)==0):
   # print('even')
#else:
    #print('odd')

#rem=num%2
#if (rem==0):
#    print('even')
#else:
#    print('odd')

print('\n')

Maths_mark=int(input('Please, input the mark of your maths subject within 100:'))
English_mark=int(input('Please, input the mark of your english subject within 100:'))

if Maths_mark>English_mark:
    print('You got more marks in Maths subject.')
else:
    print('You got more marks in English subject.')
    
print('\n')

print('calculator')

num1=float(input('Please, enter the first number.'))
num2=float(input('Please, enter the second number.'))

print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')

choice=int(input('Choice one option:'))
if choice==1:
    print('The addition of num1+num2 is',num1+num2,'.')
elif choice==2:
    print('The subtraction of num1-num2 is',num1-num2,'.')
elif choice==3:
    print('The multiplication of num1*num2 is',num1*num2,'.')
elif choice==4:
    print('The division of num1/num2 is',num1/num2,'.')
else:
    print('Your option is invaild!')

