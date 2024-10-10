#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

for num in original_array:
    greater_than_five = num + 2
    new_array.append(greater_than_five)

greater_than_five = [num for num in new_array if num > 5]

print(original_array)
print(greater_than_five)
