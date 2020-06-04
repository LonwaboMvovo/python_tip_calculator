# Total and tip calculator for a given bill, tip percentage and number of people rounded to the chosen rounding
# 01/06/2020
# Lonwabo Mvovo

# Import ceil to round totals to chosen number
from math import ceil


def rounder_upper(base_num):
    '''returns the given number rounded to the chosen number'''
    return round_to * ceil(base_num/round_to)


def money_display(amount):
    '''returns a string formated to how money is displayed'''
    return f'{currency_symbols[currency]}{round(amount, 2):.2f}'


# Dictionary of currency symbols
currency_symbols = {
    'r' : 'R',
    'p' : '£',
    'y' : '¥',
    'e' : '€',
    'd' : '$'
}

# Set 'short' initially to 0
# 'short' is the amount of money needed to be paid from rounding errors
short = 0

# Infinite loop that breaks when user enters a valid currency from the given list
while True:
        try:
            # Set 'currency' to a currency letter that corresponds to a currency symbol inputed by user
            currency = input('(R)and / (P)ound / (Y)en / (E)ure / (D)ollar: ').lower()
            # Assert that the users chosen currency is a valid currency in the list
            assert currency in currency_symbols
            break
        # Error message for when the user does not enter a valid currency from the given list
        except:
            print('Invalid input. Please input either (R) for Rand, (P) for Pound, (Y) for Yen, (E) for Euro or (D) for Dollar for the currency.')

# Infinite loop that breaks when the user enters an integer representing the number of people included in paying for the bill
while True:
    try:
        # Set 'num_ppl' to a user inputed integer representing the number of people included in paying for the bill
        num_ppl = int(input('Number of people: '))
        break
    # Error message for when the user does not enter an integer
    except ValueError:
        print('Invalid input. Please input an integer for the number of people.')

# Check if there's only one person paying for the bill
if num_ppl == 1:
    # Infinite loop that breaks when the user enters a float representing the bill amount
    while True:
        try:
            # Set 'bill' to a user inputed float representing the bill amount
            bill = float(input(f'Bill: {currency_symbols[currency]}'))
            break
        # Error message for when the user does not enter a float
        except ValueError:
            print('Invalid input. Please input a float for the bill.')

    # Infinite loop that breaks when the user enters a float representing the tip percentage
    while True:
        try:
            # Set 'tip_perc' to a user inputed float representing the tip percentage
            tip_perc = float(input('Tip percentage: '))
            break
        # Error message for when the user does not enter a float
        except ValueError:
            print('Invalid input. Please input a float for the tip percentage.')

    # Ask the user if they would like to round up their total and set 'round_up' to their answer
    round_up = input('Round up total? (Y)es or (N)o: ').lower()

    # Calculate tip amount with the given tip percentage and set that to 'tip'
    tip = bill * (tip_perc/100)
    # Calculate total amount and set that to 'total'
    total = bill + tip

    # Check if the user did want to round their total up
    if round_up == 'y':
        # Infinite loop that breaks when the user enters a number they would like to round to from the given options
        while True:
            try:
                # Set 'round_to' to an integer inputed by the user representing the number they would like to round to from the list of numbers
                round_to = int(input('Round to nearest (1), (5), (10): '))
                # Assert that the number the user has chosen is in the given options
                assert round_to == 1 or round_to == 5 or round_to == 10
                break
            # Error message for when the user does not enter an integer in the given options
            except:
                print('Invalid input. Please input either 1, 5 or 10 for the number you would like your total to be rounded to.')
        
        # Round the total using the 'rounder_uppper' function, then set total to this rounded number
        total = rounder_upper(total)

    # Print the tip total formatted using the 'money_display' function
    print('\nTip total:', money_display(tip))
    # Print the total formatted using the 'money_display' function
    print('Total:', money_display(total))
# Otherwise for when there's is more than one person paying
else:
    # Ask the user if they would like to split the bill evenly and set this answer in lowercase to 'split_even'
    split_even = input('Even split? (Y)es or (N)o: ').lower()

    # Check if the user would like to split the bill evenly
    if split_even == 'y':
        # Infinite loop that breaks when the user inputs a float for the total bill
        while True:
            try:
                # Set 'bill' to a float inputed by the user representing the total bill
                bill = float(input(f'Bill: {currency_symbols[currency]}'))
                break
            # Error message for when the user does not enter a float
            except ValueError:
                print('Invalid input. Please input a float for the bill.')

        # Infinite loop that breaks when the user inputs a float for the tip percentage
        while True:
            try:
                # Set 'tip_perc' to a float inputed by the user representing the tip percentage
                tip_perc = float(input('Tip percentage: '))
                break
            # Error message for when the user does not enter a float
            except ValueError:
                print('Invalid input. Please input a float for the tip percentage.')

        # Ask the user if they would like to round up their total and set 'round_up' to their answer
        round_up = input('Round up total? (Y)es or (N)o: ').lower()

        # Calculate tip amount with the given tip percentage and set that to 'tip'
        tip = bill * (tip_perc/100)
        # Calculate total amount and set that to 'total'
        total = bill + tip

        # Check if the user did want to round their total up
        if round_up == 'y':
            while True:
                try:
                    # Set 'round_to' to an integer inputed by the user representing the number they would like to round to from the list of numbers
                    round_to = int(input('Round to nearest (1), (5), (10): '))
                    # Assert that the number the user has chosen is in the given options
                    assert round_to == 1 or round_to == 5 or round_to == 10
                    break
                # Error message for when the user does not enter an integer in the given options
                except:
                    print('Invalid input. Please input either 1, 5 or 10 for the number you would like your total to be rounded to.')

            # Round the total using the 'rounder_uppper' function, then set total to this rounded number
            total = rounder_upper(total)

        # Calculate tip amount per person and set 'tip_pp' to that number
        tip_pp = tip / num_ppl
        # Calculate total amount per person and set 'total_pp' to that number
        total_pp = total / num_ppl

        # Round the total per person using the 'rounder_uppper' function, then set the total to this rounded number if the user did want to round their total
        if round_up == 'y':
            total_pp = rounder_upper(total_pp)

        # Print the tip per person formatted using the 'money_display' function
        print('\nTip per person:', money_display(tip_pp))
        # Print the total per person formatted using the 'money_display' function
        print('Total per person:', money_display(total_pp))

        # Calculate the difference that occurs because of rounding errors and set 'short' to this number
        short = round(total, 2) - round(total_pp, 2) * 3

        # If 'short' is negative it means that because of rounding the total and tip will be more
        if short < 0:
            # Update the tip total
            tip = tip_pp * num_ppl
            # Update the total 
            total = total_pp * num_ppl

        # Print the tip total formatted using the 'money_display' function
        print('\nTip total:', money_display(tip))
        # Print the total formatted using the 'money_display' function
        print('Total:', money_display(total))

        # Print 'short' if there is a rounding error
        if round(short, 2) > 0:
            print('\nShort:', money_display(short))
    # Otherwise for when the users would not like to split the bill evenly
    else:
        # Set 'ppl_tips' initially an empty list which represents the tip amounts per person
        ppl_tips = []
        # Set 'ppl_totals' initially an empty list which represents the total amounts per person
        ppl_totals = []

        # For each person
        for person in range(num_ppl):
            # Infinite loop that breaks when the user inputs a float for their bill
            while True:
                try:
                    # Set each persons bill to a float inputed by the user
                    person_bill = float(input(f'Person-{person + 1} bill: {currency_symbols[currency]}'))
                    break
                # Error message for when the user does not input a float for their bill amount
                except:
                    print('Invalid input. Please input a float for the bill amount.')

            # Infinite loop that breaks when the user inputs a float for what percentage they would like their tip to be
            while True:
                try:
                    # Set 'person_tip_perc' to a float inputed by the user represting a float for what percentage they would like their tip to be
                    person_tip_perc = float(input('Tip percentage: '))
                    break
                # Error message for when the user does not input a float for their tip percentage
                except ValueError:
                    print('Invalid input. Please input a float for the tip percentage.')

            # Ask the user if they would like to round up their total and set 'round_up' to their answer
            round_up = input('Round up total? (Y)es or (N)o: ').lower()

            # Calculate tip amount per person and set 'person_tip' to that number
            person_tip = person_bill * (person_tip_perc/100)
            # Calculate total amount per person and set 'person_total' to that number
            person_total = person_bill + person_tip

            # Check if the user did want to round their total up
            if round_up == 'y':
                while True:
                    try:
                        # Set 'round_to' to an integer inputed by the user representing the number they would like to round to from the list of numbers
                        round_to = int(input('Round to nearest (1), (5), (10): '))
                        assert round_to == 1 or round_to == 5 or round_to == 10
                        break
                    # Error message for when the user does not enter an integer in the given options
                    except:
                        print('Invalid input. Please input either 1, 5 or 10 for the number you would like your total to be rounded to.')

                # Round the persons total using the 'rounder_uppper' function, then set total to this rounded number
                person_total = rounder_upper(person_total)

            # Append the persons tip to 'ppl_tips'
            ppl_tips.append(person_tip)
            # Append the persons total to 'ppl_totals'
            ppl_totals.append(person_total)

        # For each person
        for i in range(num_ppl):
            # Print their tip and total formatted using the 'money_display' function
            print(f'\nPerson-{i + 1}:\nTip: {money_display(ppl_tips[i])}\nTotal: {money_display(ppl_totals[i])}')

        # Calculate tip amount by summing all the tip amounts
        tip = sum(ppl_tips)
        # Calculate total amount by summing all the totals
        total = sum(ppl_totals)

        # Print the tip total formatted using the 'money_display' function
        print('\nTip total:', money_display(tip))
        # Print the total formatted using the 'money_display' function
        print('Total:', money_display(total))