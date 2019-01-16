from Prac08.car import Taxi, SilverServiceTaxi

MENU = "Let's drive! \nq)uit. c)hoose taxi, d)rive"

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

print(MENU)
menu_choice = input(">>> ")

bill = 0
selected_taxi = 0
taxi_choice = 0
total_fare = 0

while menu_choice != "q":
    if menu_choice == "c":
        count = 0
        for index, taxi in enumerate(taxis):
            print("{}. {}".format(index, taxi))
        taxi_choice = int(input("Choose taxi "))
        selected_taxi = taxis[taxi_choice]
        print(selected_taxi)
        print("Bill to date: {}".format(bill))

    elif menu_choice == "d":
        distance = int(input("Drive how far? "))
        taxis[taxi_choice].start_fare()
        taxis[taxi_choice].drive(distance)
        fare = taxis[taxi_choice].get_fare()
        taxi_name = str(taxis[taxi_choice]).split(',', 1)
        print("Your {} trip cost you {:.2f}".format(taxi_name[0], fare))

        total_fare += fare

    print(MENU)
    menu_choice = input(">>> ")


print("Total trip cost ${:.2f}".format(total_fare))

print("Taxis are now")
for index, taxi in enumerate(taxis):
    print("{}. {}".format(index, taxi))

