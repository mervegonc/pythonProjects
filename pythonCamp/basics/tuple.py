# -*- coding: utf-8 -*-

#tuples are readonly you can't change index in the list, after creating it

tupleList = (0, 1, 2, "Ankara", (2,3,4),[])
list = [0, 1, 2, "İstanbul", [3,7,8], ()]

list[0]= 6
#tupleList[0] = 6 #'tuple' object does not support item assignment

print(tupleList[-2])#this brings the second index in the list
print(list[-2])

print(tupleList[1:2])#this brings the second index in the list
print(list[1:2])

print(type(tupleList))
print(type(list))
print(list)
print(tupleList)
print(len(tupleList))
print(len(list))