

# This is tan example of the diamond inheritance problem.
class A:
    def __init__(self):
        print("This is __init() from class A")


class B(A):
    def __init__(self):
        print("This is __init() from class B ")
        super().__init__()

class C(A):
    def __init__(self):
        print("This is __init() from class C ")
        super().__init__()


class BC(B, C):
    def __init__(self):
        print("This is __init() from class BC ")
        super().__init__()



bc = BC()  # Question here: which __init__() get called?
#c = C()    
