

MENU = "Enter C - Convert Celsius to Fahrenheit\nEnter F - Convert Fahrenheit to Celsius\nQ (for quit)"


def main():
    print(MENU)
    choice = input(" ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = float(input("Enter Fahrenheit: "))
            celsius = convert_cel_to_fah(fahrenheit)
            print("Celsius is" +celsius)
        elif choice == "F":
            celsius = float(input("Enter Celsius: "))
            convert_fah_to_cel()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(" ").upper()

    print("Thank you.")


def convert_fah_to_cel(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return  celsius


def convert_cel_to_fah(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return  fahrenheit

main()
