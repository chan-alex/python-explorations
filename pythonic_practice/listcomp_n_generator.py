

letters=["a","b","c","d","e","f"]

# this is example of a listcomp
codes = [ord(l) for l in letters]


#In Python 2.x listcomps used to leak.

x = "this is a string"
z = [x for x in letters]

# In python 2, x would have a value of "f". it has been clobbered.
# In python 2, x retains it's original value.
print(x)   



# Generators are like list comp except they are enclosed in parenthese instead
# of brackets.
genexp1 = (ord(l) for l in letters)


print(genexp1)
# prints something like:  <generator object <genexpr> at 0x1106fc048>

for g in genexp1:
    print(g)

# prints:
# 97
# 98
# 99
# 100
# 101
# 102

# The other difference between listcomp and genexp is that listcomp build lists in memory
# while genexp doesn't. They just supplied the next value one by one, on demand.
# They don't use any memory while doing it. 
