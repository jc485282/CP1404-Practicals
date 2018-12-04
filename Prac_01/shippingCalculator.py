
def main():
    required = -1
    while required <= 0:
        required = int(input("Enter the number of items being shipped"))
        itemCosts = [""] * required
    totalCost = 0
    for i in range(0,required,1):
        print("Please enter cost of item:", str(i+1))
        itemCosts[i] = int(input())
        totalCost += itemCosts[i]

    print("Number of items:", required)
    for i in range(0,required,1):
        print("Price of item:", itemCosts[i])

    if totalCost > 100:
        totalCost = totalCost * 0.9
    print("Total cost for shipping", required, "items is:", totalCost)

main()





