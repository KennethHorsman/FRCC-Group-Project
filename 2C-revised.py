""" This one is definitely a bit more complicated! A few comments:
1. Again, I would break the Income_Tax_Inputs function up into three: one to get gross income, one to get number of dependents under 6, and one to get the number of dependents over 6.

2. I wouldn't calculate the tax rate in the same function as you use to ge the inputs. I would calculate it in the main program once you have all of the necessary inputs

3. The nested if...if...if... to get the tax rate make me a bit uncomfortable. I would use something more like
if net_income < 11_000:
    tax_rate = 0
elif net_income >= 11_000 and net_income < 44_725:
    tax_rate = 0.12
...
elif net_income > 578_125:
    tax_rate = 0.37

4. It's generally not a good idea to redefine a variable (e.g. income = int(income)) - it makes it really easy to lose track of exactly what type or value a variable has and opens you up for bugs. 
It's generally better to do something like:

income_input = input("...")
income = int(income_input)

5. Under Income_Tax_Calculations, you check if the number of dependents is greater than 0. However, you don't really need this check. 
After all, if the number of dependents is 0, then 2000 * dependents_under_6 + 3000 * dependents_over_6 = 0 anyway.

"""

def is_valid_number(num: str): 
    try: 
        float(num) 
        return True
    except ValueError: 
        return False

def Income_Tax_Inputs():
       while True:
              gross_income = input("Please enter your gross income without a comma: ")
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
                     print("Your number of dependants cannot be a negative number.")
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
       return income_tax

income_tax = Income_Tax_Calculations()

gross_income = "{:,}".format(round(gross_income,2))
income_tax = "{:,}".format(round(income_tax,2))

print(f"\nGross Income: {gross_income}")
print(f"Number of dependants under 6 years old: {dependants_under_6}")
print(f"Number of dependants over 6 years old: {dependants_over_6}")
print(f"\nYour income tax is: ${income_tax}")
input('')
