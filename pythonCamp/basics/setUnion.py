# -*- coding: utf-8 -*-

setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

#birleştirir aynıolanları yazmadan
print(setA | setB)
print(setA.union(setB))

#aynı olanları yazar
print(setA & setB)
print(setA.intersection(setB))

#a da olup b de olmayanı yazar
print(setA - setB)
print(setB.difference(setA))


print(setA ^ setB)
print(setA.symmetric_difference(setB))