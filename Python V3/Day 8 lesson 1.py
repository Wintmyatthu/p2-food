
#print('\n')

planet=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
Planet=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']

##Replace
planet[4]='The red planet'
#print(planet)

##Insert
planet.append('The world')
Planet.append('The red planet')

#print(planet)
#print(Planet)

print('\n')

##append
Solar=list(('Sun','Moon','Star','Pluto'))
planet.extend(Solar)
Planet.extend(Solar)

#print(Solar)

#print('\n')

##insert
Solar.insert(3,'Darkness')
#print(Solar)

#print('\n')

Solar.extend(planet)
Solar.extend(Planet)

#print(Solar)

#print('\n')

#print(Planet)

#Sprint('\n')

mix=['Minecraft','Blox Fruit','Monster Legends','Money',25000,500,297,47,7,99,5,9]
print(mix)

popping=mix.pop()
print(mix)
print(popping)

del(mix[9])
print(mix)


