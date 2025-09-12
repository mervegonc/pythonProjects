# -*- coding: utf-8 -*-

number = int(input("Enter The Number : "))
isPrimary = True
for x in range(2,number):
    if number % x == 0:
        isPrimary = False
        break

if isPrimary:
    print(number, " is primary ")
    
else:
        print(number, " is NOT primary ")
        
        
   

    
