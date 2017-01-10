
# building a lists of the lists the right way.

def print_multi_list(mlist):
    for r in mlist:
        print(r)


# This works
list1 = [ ['-'] * 3 for i in range(3)]
print_multi_list(list1)

list1[0][0] = "X"
list1[1][1] = "X"
list1[2][2] = "X"
print_multi_list(list1)


# This looks right but is wrong.
list2 = [['_'] * 3] * 3
print_multi_list(list2)

list2[0][0] = "X"
list2[1][1] = "X"
list2[2][2] = "X"

print_multi_list(list2)

# The problem with list2 is that it behaves like this:
# r = ['-'] * 3
# list2 = []
# for i in range(3):
#   list2.append(r)   <--- the same row is appended 3 times to list2.



# list1 works because it does this:
# list1 = []
# for i in range(3):
#   r = ['-'] * 3    <--- a new list is created.
#   list1.append(r) 
