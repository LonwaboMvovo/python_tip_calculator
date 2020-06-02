# Total and tip calculator for a given bill, tip percentage and number of people rounded to the chosen rounding
# 01/06/2020
# Lonwabo Mvovo

from math import ceil


def rounder_upper(base_num):
    return round_to * ceil(base_num/round_to)


currency_symbols = {
    'r' : 'R',
    'p' : '£',
    'y' : '¥',
    'e' : '€',
    'd' : '$'
}

short = 0

num_ppl = int(input('Number of people: '))
currency = input('(R)and / (P)ound / (Y)en / (E)ure / (D)ollar: ').lower()
bill = float(input(f'Bill: {currency_symbols[currency]}'))
tip_perc = float(input('Tip percentage: '))
round_up = input('Round up? (Y)es or (N)o: ').lower()

tip = bill * (tip_perc/100)
total = bill + tip

if round_up == 'y':
    round_to = int(input('Round to nearest (1), (5), (10): '))
    tip = rounder_upper(tip)
    total = rounder_upper(total)

if num_ppl > 1:
    tip_pp = tip / num_ppl
    total_pp = total / num_ppl

    if round_up == 'y':
        tip_pp = rounder_upper(tip_pp)
        total_pp = rounder_upper(total_pp)

    print(f'Tip per person: {currency_symbols[currency]}{round(tip_pp, 2):.2f}')
    print(f'Total per person: {currency_symbols[currency]}{round(total_pp, 2):.2f}')

    short = round(total, 2) - round(total_pp, 2) * 3

    if short < 0:
        tip = tip_pp * num_ppl
        total = total_pp * num_ppl

print(f'Tip: {currency_symbols[currency]}{round(tip, 2):.2f}')
print(f'Total: {currency_symbols[currency]}{round(total, 2):.2f}')

if round(short, 2) > 0:
    print(f'Short: {currency_symbols[currency]}{round(short, 2):.2f}')