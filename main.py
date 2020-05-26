from math import ceil

currency = input('Currency: ')
bill = float(input('Bill Amount: '))
tip_percent = float(input('Tip Percent: '))
num_ppl = int(input('How many people to divide by: '))
round_up = input(f'Round to nearest {currency} (y)es or (n)o: ')

tip = bill * (tip_percent / 100)
total = bill + bill * (tip_percent / 100)
tip_pp = tip / num_ppl
total_pp = total / num_ppl

print(f'\nTotal: {currency}{ceil(total) if round_up == "y" else round(total, 2)}')
print(f'Total (per person): {currency}{ceil(total_pp) if round_up == "y" else round(total_pp, 2)}')
print(f'Tip: {currency}{ceil(tip) if round_up == "y" else round(tip, 2)}')
print(f'Tip (per person): {currency}{ceil(tip_pp) if round_up == "y" else round(tip_pp, 2)}')