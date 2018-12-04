def main():
    name = get_name()
    print_name(name)


def print_name(name):
    for char in range(1, (len(name)), 2):
        print(name[char])


def get_name():
    name = input('please enter your name')
    while name == "":
        print('you are required to enter something')
        name = input('please enter your name')
    return name

main()
