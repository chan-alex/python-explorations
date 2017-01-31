

# The state pattern is basically implementing a state machine in an object oriented way.
# The other ways of implement a state machine is via if-else statements.
# From the UML point of way, it is similar to the Strategy pattern.
 



class GreenLight():

    def transition(self, trafficlight):
        trafficlight.current_state = AmberLight()

    def __str__(self):
        return "Green Light"

    
class AmberLight():

    def transition(self, trafficlight):
        trafficlight.current_state = RedLight()

    def __str__(self):
        return "Amber Light"

    
class RedLight():

    def transition(self, trafficlight):
        trafficlight.current_state = GreenLight()

    def __str__(self):
        return "Red Light"

    
    
class TrafficLight:

    def __init__(self):
        self.current_state = GreenLight()

    def transition(self):
        self.current_state.transition(self)

    def __str__(self):
        return self.current_state.__str__()

    
def test():

    TL = TrafficLight()

    print(TL)
    TL.transition()
    print(TL)
    TL.transition()
    print(TL)
    TL.transition()
    print(TL)
    TL.transition()
    print(TL)
