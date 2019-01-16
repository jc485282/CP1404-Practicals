from Prac07.guitar import Guitar


def main():
    guitars = []

    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        name = Guitar(name, year, cost)
        print("{self.name} ({self.year}) : ${self.cost:.2f} added".format(self=name))
        guitars.append(name)

        name = input("Name: ")

    # Add some guitars
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars")

    longest_name = max(len(guitar.name) for guitar in guitars)
    longest_cost = max(len("{:.2f}".format(guitar.cost)) for guitar in guitars)

    for index, guitar in enumerate(guitars):
        vintage_status = "(vintage)" if guitar.is_vintage() else ""

        print("Guitar {0}: {self.name:>{1}} ({self.year}), worth "
              "${self.cost:<{2},.2f} {3}".format(index + 1, longest_name, longest_cost, vintage_status, self=guitar))


main()
