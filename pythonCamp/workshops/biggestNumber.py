# -*- coding: utf-8 -*-

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))


biggestNumber = number1

if number2>biggestNumber:
    biggestNumber = number2
if number3>biggestNumber:
    biggestNumber = number3


print("The biggest number is:", biggestNumber)
    