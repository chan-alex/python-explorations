
import time


# The decorator pattern is to wrap an object in some way that modify it behavior without
# modifying it's interface.

# Another use of the decorator pattern is to supporting multiple optional behaviors.
# This is a suitable alternative to multiple inheritance.

# How do you choose between decorator and inhertiance?
# One way to choose is to use decorators when modify the target dynamically based on
# some confition


def execute(action):
    action()

def action1():
    print("Doing some action")


# This is one way to create a decorator 
class TimeAction:

    def __init__(self, action):
        self.action = action

    def __call__(self):
        print("Start time: {}".format(time.time()))
        self.action()
        print("End time: {}".format(time.time()))

class LogAction:

    def __init__(self, action):
        self.action = action

    def __call__(self):
        print("Logging the start of action...")
        self.action()
        print("Logging the end of action...")


# Another way to implement decorator might be with python builtin decorators.
# This is a very simple example.
def TimeAction1(action):
    def wrapper():
        print("Start time: {}".format(time.time()))
        action()
        print("End time: {}".format(time.time()))
    return wrapper    
        
@TimeAction1
def action2():
    print("this is action 2")
        

def test():

    print("Just executing action1. No decorator")
    execute(action1)
    print("-------------------------")

    
    print("Executing action1 with decorator style 1\n")    
    execute(TimeAction(action1))
    print(" ")
    execute(LogAction(action1))

    print("-------------------------")

    print("Executing action2 with python style decorator\n")       
    action2()

    
