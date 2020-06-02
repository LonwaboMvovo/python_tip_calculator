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

num_ppl = int(input('Number of people: '))
currency = input('(R)and / (P)ound / (Y)en / (E)ure / (D)ollar: ').lower()
bill = float(input(f'Bill: {currency_symbols[currency]}'))
tip_perc = float(input('Tip percentage: '))
round_up = input('Round up? (Y)es or (N)o: ').lower()

if round_up == 'y':
    round_to = int(input('Round to nearest (1), (5), (10): '))
    tip = rounder_upper(bill * (tip_perc/100))
    total = rounder_upper(bill) + tip
else:
    tip = bill * (tip_perc/100)
    total = bill + tip

print(f'Tip: {currency_symbols[currency]}{round(tip, 2):.2f}')
print(f'Total: {currency_symbols[currency]}{round(total, 2):.2f}')

if num_ppl > 1:
    if round_up == 'y':
        tip_pp = rounder_upper(tip / num_ppl)
        total_pp = rounder_upper(total / num_ppl)
    else:
        tip_pp = tip / num_ppl
        total_pp = total / num_ppl 

    print(f'Tip per person: {currency_symbols[currency]}{round(tip_pp, 2):.2f}')
    print(f'Total per person: {currency_symbols[currency]}{round(total_pp, 2):.2f}')

    short = total - round(total_pp, 2) * 3
    if short > 0:
        print(f'Short: {currency_symbols[currency]}{round(short, 2):.2f}')