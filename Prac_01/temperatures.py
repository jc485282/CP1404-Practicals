

MENU = "Enter C - for converting celsius to Fahrenheit, Enter F - Convert Fahrenheit to Celsius\nQ (for quit)"
print(MENU)
choice = input("Enter your Choice ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Fahrenheit: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print("Celsius is {:.2f} C".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input("Enter choice").upper()

