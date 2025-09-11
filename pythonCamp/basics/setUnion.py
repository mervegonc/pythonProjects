# -*- coding: utf-8 -*-

setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

#birleştirir aynıolanları yazmadan
print(setA | setB)
print(setA.union(setB))

#it writes the same ones
print(setA & setB)
print(setA.intersection(setB))

#it writes the ones that are in a but not in b in order.
print(setA - setB)
print(setB.difference(setA))


#Here, it writes the items that are in a but not in b, and the items that are in b but not in a.
print(setA ^ setB)
print(setA.symmetric_difference(setB))
