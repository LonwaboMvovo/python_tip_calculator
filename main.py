# Total and tip calculator for a given bill, tip percentage and number of people rounded to the chosen rounding
# 01/06/2020
# Lonwabo Mvovo

num_ppl = int(input('Number of people: '))
bill = float(input('Bill: '))
tip_perc = float(input('Tip percentage: '))
tip = bill * (tip_perc/100)
total = bill + tip

print(f'Tip: {round(tip, 2):.2f}')
print(f'Total: {round(total, 2):.2f}')

if num_ppl > 1:
    tip_pp = tip / num_ppl
    total_pp = total / num_ppl 

    print(f'Tip per person: {round(tip_pp, 2):.2f}')
    print(f'Total per person: {round(total_pp, 2):.2f}')

    short = total - round(total_pp, 2) * 3
    if short > 0:
        print(f'Short: {round(short, 2):.2f}')