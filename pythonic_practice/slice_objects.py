#!/usr/bin/env python3

print("start")


list_of_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


# Sequence slices actually return Slice object.
# The 2 expression below are equivalent:

list_of_numbers[1:5]
# >>> list_of_numbers[1:5]
# [2, 3, 4, 5]

list_of_numbers[slice(1,5)]
# >>> list_of_numbers[slice(1,5)] 
# [2, 3, 4, 5


# The useful thing about slice objects is that you can name them.

first_10 = slice(0,10)
next_10 = slice(10,20)

print(list_of_numbers[first_10])
print(list_of_numbers[next_10])
