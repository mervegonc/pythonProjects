# -*- coding: utf-8 -*-
"""
student1 = "Merve"
student2 =  "Engin"
student3 =  "Seyfi"
print(student1)
print(student2)
print(student3)

students = ["Merve","Engin","Seyfi"]

print(students[1])
students.append("Ayşe")
students.remove("Engin")
print(students)
"""
#list constructor
cities = list(("Ankara", "İstanbul", "Ankara"))
print(cities)
print(len(cities))

#other fonctions
"""print(cities.clear())
print(cities)
"""
print("Ankara = " + str(cities.count("Ankara")))
print(cities)

print("Ankara total index = " + str(cities.index("Ankara")))
print(cities)

cities.pop(1)
cities.insert(0,"İstanbul")
cities.reverse()
print(cities)

cities2 = cities
cities2[0] = "İzmir"
print(cities2)
print(cities)