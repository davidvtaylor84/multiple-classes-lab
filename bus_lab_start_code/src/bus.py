class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []
        
    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, passenger1):
        self.passengers.append(passenger1)

    def drop_off(self, passenger1):
        self.passengers.remove(passenger1)

    def empty(self):
        self.passengers.clear()

    def pick_up_from_stop(self, bus_stop):
        for passenger in bus_stop.queue:
            if passenger:
                self.pick_up(passenger)

    # def pick_up_from_stop(self, bus_stop_to_pick_up_from):
    #     for passenger in bus_stop_to_pick_up_from.queue:
    #         self.pick_up(passenger)
    #     bus_stop_to_pick_up_from.clear()

