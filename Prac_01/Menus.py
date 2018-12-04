name = input('Enter your name\n')
menu = '--Main menu--\n(H)ello \n(G)oodbye \n(Q)uit\n'
print(menu)
menu_choice = input(">>> ").upper()
while menu_choice != 'Q':
    if menu_choice == 'H':
        print('Hello', name )
    elif menu_choice == 'G':
        print('Goodbye', name)
    else:
        print('Input not recognised')
    print(menu)
    menu_choice = input(">>> ").upper()
print('Mission complete')
