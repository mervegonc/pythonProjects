# -*- coding: utf-8 -*-

cities = ["Ankara", "İstanbul", "Çorum"]
print(cities[0])
print(cities[1])
print(cities[2])

for city in cities:
    print(city + "'s code is: " + city[0:3])
    
    
for city in cities:
    if city == "Ankara":
        print(city + "s code is: " + city[0:3])
  