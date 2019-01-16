from Prac08.car import UnreliableCar

new_mazda = UnreliableCar("2010 Mazda", 100, 95)
new_mazda.drive(60)
print(new_mazda)
new_mazda.drive(30)
print(new_mazda)
print()

old_mazda = UnreliableCar("1982 Mazda", 100, 50)
old_mazda.drive(60)
print(old_mazda)
old_mazda.drive(30)
print(old_mazda)
