def main():
    item_name = input("Item name: ")
    while item_name == "" or " " in item_name:
        print("Input can not be blank")
        item_name = input("Item name: ")

    item_name = item_name[0].upper() + item_name[1:].lower()
    print(item_name)
main()
