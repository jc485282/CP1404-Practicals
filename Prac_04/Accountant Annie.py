


def main():
    incomes = []
    months = int(input("How many months? "))

    for i in range(1, months + 1):
        income = float(input("Enter income for month {}".format(i)))
        incomes.append(income)

    print_income_report(incomes, months)


def print_income_report(incomes, months):
    print("\nIncome Report\n-------------")
    total = 0
    for i in range(1, months + 1):
        income = incomes[i - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(i, income, total))


main()
