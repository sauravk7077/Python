from array import array

# lists

scores = []

scores.append(98)
scores.append(78)
print(scores)
print(scores[0])

# array (allows only a certain type)
scored = array('d')
scored.append(88)
scored.append(79)

print(scored)

#common functions
print(len(scored))
scores.insert(0,79)
print(scores)
scores.sort()
print(scores)

# dictionary

name = {}
name['first'] = 'Ro'
name['last'] = 'Po'

name2 = {}
name2['first'] = 'Do'
name2['last'] = 'Go'

#Combining list and dictionary

people = []
people.append(name)
people.append(name2)
people.append({
    'first':'Ao', 'last':'Oa'
})

print(people)