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