# -*- coding: utf-8 -*-

number = int(input("How many stars do you want? "))

stars =""
for x in range(1,number+1):
    stars = stars + "*"
    print(stars)