

# Reversed() take a sequence and return a reverseiterator object.
# Usually used in a for loop.

a = [1,2,3,4,5]

for x in reversed(a):
    print(x)


# reversed() works by calling the __reversed__() of the object.
# By re-defining __reversed__() it is possible to optimize this opertion.
class WeirdSeq():

    def __reversed__(self):
        return "Weird stuff"

w = WeirdSeq()
for x in reversed(w):
    print(x)


# If __reversed__() is not available, reversed() will try to use __len__() and
# __getitem__().
class StrangeSeq():
    _string = "This is a strange sequence"

    def __len__(self):
        return len(self._string)

    def __getitem__(self, index):
        return 'X'


sq = StrangeSeq()
for x in reversed(sq):
    print(x)
