LOWER =33
UPPER = 100
print("Enter a number ({}) - ({})".format(LOWER, UPPER))
num= input()
print("for"+ num+ "ascii is "+ chr(num))
for i in range(34, 127, 1):
    print("{:<4d} {}".format(i, chr(i)))