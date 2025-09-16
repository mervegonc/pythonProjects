# -*- coding: utf-8 -*-

city = "Ankara"

print(city.upper())
print(city.endswith("a"))#it turns false or true

def sayHi(name = "dearist"):
    print("Hello " + name)
 
    
def sayHi2(name, surName = "friend"):
    print("Hello " + name + " " + surName)
    
    
sayHi()
sayHi("Merve")
sayHi2("Arzu", "Köncü")
sayHi2("Arzu")

def rightTriangleCalculate(a,b):
    return a*b/2

print(rightTriangleCalculate(2, 6))

#&&
rightTriangleCalculate2 = lambda a,b : a*b/2

print(rightTriangleCalculate2(3,8))
print(type(rightTriangleCalculate2))