#!/usr/bin/env python3

print("Start")


# Slices can be used to modify a mutable sequence in place.
list1 = list(range(10))

print(list1)

#Assignment.
list1[2:3] = ["a", "b"]
print(list1)
# [0, 1, 'a', 'b', 3, 4, 5, 6, 7, 8, 9]


list1[2:4] = "X"   # just to show this works too.
print(list1)
# [0, 1, 'X', 3, 4, 5, 6, 7, 8, 9]   notice the list is shorter. 1 menmber got deleted.


# This is delete.
del list1[1:3]
print(list1)
# [0, 3, 4, 5, 6, 7, 8, 9]


# the above does not work with strings. It's not a mutable sequence.
# string1="qwertyuiop"
# string1[2:5] = [1,2,3]
# print(string1)



# Multiplication
list2 = [ 1, 2] * 5
print(list2)
# [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]



