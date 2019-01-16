#
# def print_countdown(number=3):
#     print(number)
#     while number > 0:
#         number -= 1
#         print(number)
#
# print_countdown()


# def lynds_print_countdown(number=3):
#     for i in range(number, -1, -1):
#         print(i)
#
# lynds_print_countdown()

#recursion

# def recurse(n):
#     if n <= 0:
#         print("Thing!")
#     else:
#         print(n)
#         recurse(n-1)
#         print(n)
#
# recurse(4)

# TODO: ask for thisone
# def recursion_print_sum_countdown(n):
#     # write a recursive function to add up the numbers from 0 to n
#     # for i in range(number, -1, -1):
#     #     recursion_print_countdown(i-1)
#     #     # print(i)
#
#     if n < 0:
#         return 0
#     print(n)
#     return n * recursion_print_sum_countdown(n - 1)
#
# recursion_print_sum_countdown(4)

# def recursion_print_countdown(n):
#     # if n == 0:
#     #     print(0)
#     # else:
#     #     print(n)
#     #     recursion_print_countdown(n - 1)
#
#     print(n)
#     if n != 0:
#         recursion_print_countdown(n-1)
#
# recursion_print_countdown(4)


# doing some assert to check
def is_odd(n):
    return n % 2

for i in range(1, 10, 2):
    assert is_odd(i)

for i in range(0, 10, 2):
    assert not is_odd(i)


