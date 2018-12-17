

COLOUR_NAMES = {"AliceBlue": "f0f8ff", "Black": "000000", "CadetBlue": "5f9ea0", "Chocolate": "d2691e",
                "CornflowerBlue": "6495ed", "DarkGreen": "006400", "DarkSalmon": "e9967a"}

colour = input("Enter colour: ")
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ")

for colour, hex_value in COLOUR_NAMES.items():
    print("{:<15} is {:<5}".format(colour, hex_value))
