motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#APPENDING LIST
motorcycles.append('ducati')
print(motorcycles)

#MODIFIING LIST
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = [] 
motorcycles.append('honda') 
motorcycles.append('yamaha') 
motorcycles.append('suzuki')
print(motorcycles)

#INSERTING LIST
motorcycles.insert(0, 'ducati')
print(motorcycles)

#DELETING LIST
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
del motorcycles[0] 
print(motorcycles)


#POP LIST
#The pop() method removes the last item in a list, 
#but it lets you work with that item after removing it
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop() 
print(motorcycles)
print(popped_motorcycle)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki'] 
last_owned = motorcycles.pop() 
print(f"The last motorcycle I owned was a {last_owned.title()}.")