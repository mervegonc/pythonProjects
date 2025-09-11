# -*- coding: utf-8 -*-

studentsSet = {"Merve", "Arzu","Melike"}
print(studentsSet)

for student in studentsSet:
    print(student)
    
    
print("Merve" in studentsSet)

if "Merve" in studentsSet:
    print("is in the list")
    
studentsSet.add("Mera")
print(studentsSet)    

studentsSet.update(["Ahmet", "Mert", "Selin"])
print(studentsSet)
print(len(studentsSet))

print(studentsSet.remove("Selin"))
print(len(studentsSet))

studentsSet.discard("Selin")
print(len(studentsSet))

x = studentsSet.pop()#it deleted it as it pleased.
print(len(studentsSet))
print(studentsSet)

