import random

number_q_picks = int(input("How many quick picks would you like to generate? "))
for line in range(0, number_q_picks):
    quick_pick_list = []
    for i in range(0, 6):
        calculated_int = random.randint(1, 45)

        #if number already in list, calculate again
        while calculated_int in quick_pick_list:
            calculated_int = random.randint(1, 45)

        quick_pick_list.append(calculated_int)


    #sorting, formatting and printing
    for value in sorted(quick_pick_list):
        print("{:2}".format(value),end=" ")
    print()

