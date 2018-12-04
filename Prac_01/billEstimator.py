TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tarrif = 0



while tarrif == 0:
    tarrif_choice = int(input('Which tariff? 11 or 31:'))
    if tarrif_choice == 11:
        tarrif = TARIFF_11
    elif tarrif_choice == 31:
        tarrif = TARIFF_31
    else:
        print('Incorrect input')
daily_use = float(input('Enter daily use in kWh:'))
billing_days = int(input('Enter number of billing days:'))

estimated_bill = tarrif * daily_use * billing_days
print('\nEstimated bill: ${:.2f}'.format(estimated_bill))
