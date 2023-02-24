"""
Project 2C:

Write a program that will compute a single filer's income tax.

1. Significant constants:
       tax rate -
              37% for above $578,125 
              35% for above $231,250 
              32% for above $182,100
              24% for above $95,375 
              22% for above $44,725 
              12% for above $11,000 
       standard deduction -
              $13,850 
       deduction per dependent -
              $2,000 for <=5 or $3,000 for 6-17 (not over 17)
2. The inputs are:
       gross income 
       number of dependents 
3. Computations:
       net income = gross income - the standard deduction - a deduction for each dependent 
       income tax = is a fixed percentage of the net income 
4. The outputs are:
       the income tax, rounded to two decimals.
"""

def is_valid_number(num): 
    try: 
        float(num) 
        return True
    except ValueError: 
        return False

def Income_Tax_Inputs():
       while True:
              gross_income = input("Please enter your gross income: ")
              gross_income = gross_income.replace(",", "")
              if not is_valid_number(gross_income):
                     print("Invalid character(s) detected.")
                     continue
              elif float(gross_income) < 0:
                     print("Your gross income must be a positive number.")
                     continue
              else:
                     gross_income = float(gross_income)
                     break

       while True:
              num_dependants = input("Please enter your number of dependants: ")
              if not num_dependants.isdigit():
                     print("Invalid character(s) detected.")
              elif int(num_dependants) < 0:
                     print("Your number of dependants must be a positive number.")
              else:
                     num_dependants = int(num_dependants)
                     dependants_over_6 = 0
                     dependants_under_6 = 0
                     if num_dependants > 0: 
                            for x in range(num_dependants):
                                   while True:
                                          dependant_age = input(f"Is dependant {x+1} at least 6 years old? Enter 'YES' or 'NO': ")
                                          if dependant_age == "YES":
                                                 dependants_over_6 += 1
                                                 break
                                          elif dependant_age == "NO":
                                                 dependants_under_6 += 1
                                                 break
                                          else:
                                                 print("Invalid character(s) detected.")
                     else:
                            dependants_over_6 = 0
                            dependants_under_6 = 0
                     break
       return gross_income, num_dependants, dependants_over_6, dependants_under_6     

gross_income, num_dependants, dependants_over_6, dependants_under_6 = Income_Tax_Inputs()         

def Income_Tax_Calculations():
       if num_dependants > 0:
              dependant_deduction = (2000 * dependants_under_6) + (3000 * dependants_over_6)
       else:
              dependant_deduction = 0

       standard_deduction = 13850
       net_income = gross_income - standard_deduction - dependant_deduction
       if net_income > 11000:
              tax_rate = 0.12
              if net_income > 44725:
                     tax_rate = 0.22
                     if net_income > 95375:
                            tax_rate = 0.24
                            if net_income > 182100:
                                   tax_rate = 0.32
                                   if net_income > 231250:
                                          tax_rate = 0.35
                                          if net_income > 578125:
                                                 tax_rate = 0.37
       else:
              tax_rate = 0

       income_tax = tax_rate * net_income
       return income_tax, net_income

income_tax, net_income = Income_Tax_Calculations()
net_income = "{:,.2f}".format(net_income)
income_tax = "{:,.2f}".format(income_tax)

print(f"\nYour Net Income: ${net_income}\nYour Income Tax: ${income_tax}")
input('')