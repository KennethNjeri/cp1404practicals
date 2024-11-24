from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flag_fall = 4.50
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def get_fare(self):
        return self.flag_fall + super().get_fare()

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, ${self.price_per_km:.2f}/km plus flag fall of ${self.flag_fall:.2f}"

