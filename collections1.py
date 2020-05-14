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

#Tuples - These are immuatable
#Empty tuple
tuple1 = () # or tuple()
objects = ('car','pen','modem','monitor')

print(objects)

#Sets - Unordered collection with property to remove duplicates

#Empty Sets
empty_set = set()

set1 = {'card','cloth','paper','tissue'}
set2 = {'money','card','bag','hammer'}
print(set1)

print(set1.intersection(set2))

print(set1.union(set2))

print(set1.difference(set2))
