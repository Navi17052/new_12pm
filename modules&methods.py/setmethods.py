"""s1={101,102,103,101,104,103,102,106,109}
print(s1)"""


#update the set
s1={101,102,103,101,104,103,102,106,109}
s2={101,110,11,111,123,125,104}
"""s1.add(109)
print(s1)
s1.update({107,110})
print(s1)"""
print(s1.union(s2))
print(s1 |s2) #union operator

print(s1.intersection(s2))
print(s1&s2)  #intersection operator
print(s1.difference(s2))

print(s1-s2) #difference operator
print(s1.symmetric_difference(s2))
print(s1^s2)   #symetric difference operator

s1.remove(101)
print(s1)

s1.clear()
print(s1)

s2.discard(102)  #discard does not raise error if element is not present
print(s2)