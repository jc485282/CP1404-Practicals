from Prac08.car import Taxi, SilverServiceTaxi

taxi = Taxi("Prius 1", 100)
taxi.start_fare()
taxi.drive(30)
taxi.get_fare()
print()

hummer = SilverServiceTaxi("Richa's sedan", 200, 2)
hummer.start_fare()
hummer.drive(10)
hummer.get_fare()
print(hummer)
