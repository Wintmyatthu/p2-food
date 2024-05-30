planet=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']

planett=list(('Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune'))

##Replace
#planet[2]='World'
#print(planet)

##append
#planett.append('Pluto')
#print(planett)

##insert
planet.insert(2,'World')
print(planet)

##extend
#solar=['moon','sun','stars']

#planet.extend(solar)
#print(planet)

#solar.extend(planet)
#print(solar)

del(planet[2])
print(planet)