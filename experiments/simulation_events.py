
class SimulatedEvent:

    def __init__(self, starttime, duration, id):
        self.starttime = starttime
        self.duration = duration
        self.id = id

    def execute_start(self):
        print("Event {} started".format(self.id))

    def execute_stop(self):
        print("Event {} stopped".format(self.id))


        
class SimulationScheduler:

    def __init__(self):
        self.time = 0
        self.events = []

    def add_event(self, e):
        self.events.append(e)

    def run(self):

        while True:
            print("Current time is: {}".format(self.time))

            for e in self.events:
                if e.starttime == self.time:
                    e.execute_start()

                if e.starttime + e.duration == self.time:
                    e.execute_stop()

            
            key = input("Press a key to advance time. q to quit. ")
            self.time += 1
            
            if key == 'q':
                print("q was pressed.\n")
                break






def main():

    S = SimulationScheduler()

    S.add_event(SimulatedEvent(2,5, "event_1"))
    S.add_event(SimulatedEvent(2,5, "event_2"))
    S.add_event(SimulatedEvent(3,4, "event_3"))    
    S.add_event(SimulatedEvent(1,8, "event_4"))
    S.run()
