import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')
args = parser.parse_args()

param_error = False
if args.type != 'annuity' and args.type != 'diff':
    param_error = True
    print("Incorrect parameters")
elif args.type == 'diff' and args.payment is not None:
    param_error = True
    print("Incorrect parameters")
elif args.interest is None:
    param_error = True
    print("Incorrect parameters")

if not param_error:
    parameter = ''
    if args.periods is None:
        parameter = 'n'
    elif args.type == 'annuity' and args.payment is None:
        parameter = 'a'
    elif args.principal is None:
        parameter = 'p'
    elif args.type == 'diff' and args.payment is None:
        parameter = 'd'

    if parameter == 'n':
        loan_principal = int(args.principal)
        monthly_payment = float(args.payment)
        loan_interest = float(args.interest)
        i = loan_interest / (12 * 100)
        periods = math.ceil(math.log(monthly_payment / (monthly_payment - i * loan_principal), 1 + i))
        years = periods // 12
        months = periods % 12
        years_string = ''
        months_string = ''
        and_string = ''
        if years == 1:
            years_string = '1 year'
        elif years > 1:
            years_string = str(years) + ' years'
        if months == 1:
            months_string = '1 month'
        elif months > 1:
            months_string = str(months) + ' months'
        if years_string != '' and months_string != '':
            and_string = ' and '
        print(f"It will take {years_string}{and_string}{months_string} to repay this loan!")
        print(f"Overpayment = {int(monthly_payment * periods - loan_principal)}")

    elif parameter == 'a':
        loan_principal = int(args.principal)
        periods = int(args.periods)
        loan_interest = float(args.interest)
        i = loan_interest / (12 * 100)
        monthly_payment = math.ceil(loan_principal * i * pow(1 + i, periods) / (pow(1 + i, periods) - 1))
        print(f"Your annuity payment = {monthly_payment}!")
        print(f"Overpayment = {int(monthly_payment * periods - loan_principal)}")

    elif parameter == 'p':
        monthly_payment = float(args.payment)
        periods = int(args.periods)
        loan_interest = float(args.interest)
        i = loan_interest / (12 * 100)
        loan_principal = math.floor(monthly_payment / (i * pow(1 + i, periods) / (pow(1 + i, periods) - 1)))
        print(f"Your loan principal = {loan_principal}!")
        print(f"Overpayment = {int(monthly_payment * periods - loan_principal)}")

    elif parameter == 'd':
        loan_principal = int(args.principal)
        periods = int(args.periods)
        loan_interest = float(args.interest)
        i = loan_interest / (12 * 100)
        sum_ = 0
        for m in range(1, periods + 1):
            diff_payment = math.ceil(
                loan_principal / periods + i * (loan_principal - loan_principal * (m - 1) / periods))
            sum_ += diff_payment
            print(f"Month {m}: payment is {diff_payment}")
        print(f"\nOverpayment = {sum_ - loan_principal}")
