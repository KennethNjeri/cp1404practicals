from prac_09.car import Car
import random

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.randint(1, 100)
        if random_number < self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
