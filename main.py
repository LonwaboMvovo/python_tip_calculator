# Total and tip calculator for a given bill, tip percentage and number of people rounded to the chosen rounding
# 01/06/2020
# Lonwabo Mvovo

from math import ceil


def rounder_upper(base_num):
    return round_to * ceil(base_num/round_to)


def money_display(amount):
    return f'{currency_symbols[currency]}{round(amount, 2):.2f}'


currency_symbols = {
    'r' : 'R',
    'p' : '£',
    'y' : '¥',
    'e' : '€',
    'd' : '$'
}

short = 0

while True:
    try:
        num_ppl = int(input('Number of people: '))
        break
    except ValueError:
        print('Invalid input. Please input an integer for the number of people.')

while True:
    try:
        currency = input('(R)and / (P)ound / (Y)en / (E)ure / (D)ollar: ').lower()
        assert currency == 'r' or currency == 'p' or currency == 'y' or currency == 'e' or currency == 'd'
        break
    except:
        print('Invalid input. Please input either (R) for Rand, (P) for Pound, (Y) for Yen, (E) for Euro or (D) for Dollar for the currency.')

while True:
    try:
        bill = float(input(f'Bill: {currency_symbols[currency]}'))
        break
    except ValueError:
        print('Invalid input. Please input a float for the bill.')

while True:
    try:
        tip_perc = float(input('Tip percentage: '))
        break
    except ValueError:
        print('Invalid input. Please input a float for the tip percentage.')

round_up = input('Round up? (Y)es or (N)o: ').lower()

tip = bill * (tip_perc/100)
total = bill + tip

if round_up == 'y':
    while True:
        try:
            round_to = int(input('Round to nearest (1), (5), (10): '))
            assert round_to == 1 or round_to == 5 or round_to == 10
            break
        except:
            print('Invalid input. Please input either 1, 5 or 10 for the number you would like your total to be rounded to.')
    total = rounder_upper(total)

if num_ppl > 1:
    tip_pp = tip / num_ppl
    total_pp = total / num_ppl

    if round_up == 'y':
        total_pp = rounder_upper(total_pp)

    print('Tip per person:', money_display(tip_pp))
    print('Total per person:', money_display(total_pp))

    short = round(total, 2) - round(total_pp, 2) * 3

    if short < 0:
        tip = tip_pp * num_ppl
        total = total_pp * num_ppl

print('Tip:', money_display(tip))
print('Total:', money_display(total))

if round(short, 2) > 0:
    print('Short:', money_display(short))