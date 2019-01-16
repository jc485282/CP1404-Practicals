"""
CP1404/CP5632 Practical
Car class
"""
import random


class Car:
    """ represent a car object """

    def __init__(self, fuel=0):
        """ initialise a Car instance """
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return "fuel={}, odo={}".format(self.fuel, self.odometer)

    def add_fuel(self, amount):
        """ add amount to the car's fuel"""
        self.fuel += amount

    def drive(self, distance):
        """ drive the car a given distance if it has enough fuel or drive until fuel runs out
        return the distance actually driven """
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
            distance_driven = distance
        self.odometer += distance_driven
        return distance_driven


class Taxi(Car):
    """ specialised version of a Car that includes fare costs """

    def __init__(self, name, fuel):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(name, fuel)
        self.price_per_km = 1.2
        self.current_fare_distance = 0

    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(), self.current_fare_distance,
                                                             self.price_per_km)

    def get_fare(self):
        """ get the price for the taxi trip """
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """ begin a new fare """
        self.current_fare_distance = 0

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        """ specialised version of a Taxi that includes fanciness """
        super().__init__(name, fuel)
        self.price_per_km *= float(fanciness)
        self.flagfall = 4.50

    def get_fare(self):
        """ get the price for the taxi trip """
        return self.price_per_km * self.current_fare_distance + self.flagfall

    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of {:.2f} flagfall"\
            .format(super().__str__(), self.current_fare_distance, self.price_per_km, self.flagfall)


class UnreliableCar(Car):
    """ specialised version of a Car that includes reliability - chance that drive method will work """

    def __init__(self, name, fuel, reliability):
        """ initialise a UnreliableCar instance, based on parent class Car """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """ drive like parent Car but only when randint is greater reliability car will drive """
        if self.reliability > random.randint(1, 100):
            return super().drive(distance)
        else:
            return distance
