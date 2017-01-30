
# A simple example of the observer pattern

class  EventNotifier():
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.__call__()

def observer1():
    print("this is observer1")


class Observer3():
    def __init__(self):
        self.msg = "this is observer3"

    def __call__(self):
        print(self.msg)
        
def test():

    event_notifier = EventNotifier()

    event_notifier.subscribe(observer1)
    event_notifier.subscribe(lambda: print("this is observer2"))

    observer3 = Observer3()
    event_notifier.subscribe(observer3)
    event_notifier.notify()

    
