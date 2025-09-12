# -*- coding: utf-8 -*-

number = int(input("Enter The Number : "))
isPrime = True
for x in range(2,number):
    if number % x == 0:
        isPrime = False
        break

if isPrime:
    print(number, " is prime number")
    
else:
        print(number, " is not prime number")
        
        
   

    
