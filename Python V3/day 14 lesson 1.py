"""x=1
y=5
while x<=y:
    print(x)
    x=x+1
    
print('\n')

X=1
Y=5
for i in range(0,5):
    print(X)
    X=X+1"""
    
print('\n')

print('Notice!')
print('This is a vote about which game is the best in 2023')

print('\n')

Best_games_of_2023=['1. Blox Fruits','2. Flag Wars','3. Minecraft','4. FC 24 Mobile','5. Monster Legends']
for l in Best_games_of_2023:
    print(l)
    
print('\n')
print('Which game is your favourite?')
IN=input(str('Write the number of the game! :'))
    
if IN=='1':
    print('Honestly, that is a very good choice! Your vote have been inputted')
elif IN=='2':

    print('Honestly, that is a very good choice! Your vote have been inputted')
elif IN=='3':
    print('Honestly, that is a very good choice! Your vote have been inputted')
elif IN=='4':
    print('Honestly, that is a very good choice! Your vote have been inputted')
elif IN=='5':
    print('Honestly, that is a very good choice! Your vote have been inputted')
else:
    print('Input invaild!')
    
print('\n')

total= int(0)
num= int(input('Enter a number! :'))

while num!=0:
    total+=num
    num= int(input('Enter a number! :'))
print('The total is ',total)   
    
    