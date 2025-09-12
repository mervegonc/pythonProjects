# -*- coding: utf-8 -*-

counter = 1
result = 0

while counter <= 10:
    result += counter
    counter += 1  # This line was missing

print(f"The sum of numbers from 1 to 10 is: {result}")