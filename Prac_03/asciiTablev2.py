LOWER = 10
UPPER = 100

def main():
    character = input('please enter a character: ')
    print('The ASCII code for {} is {}'.format(character,ord(character)))

    get_number(LOWER,UPPER)


def get_number(lower,upper):
    number = int(input('please enter a number between 10 and 50: '))
    while number < lower or number > upper:
        print('please enter a valid number!')
        number = int(input('please enter a number between 10 and 50: '))
    print('The character for {} is {}'.format(number, chr(number)))

main()