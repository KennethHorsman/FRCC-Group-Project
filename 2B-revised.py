""" Again, this generally looks good. I would split the Rental_Cost function up into get_num_dvds, get_num_vhs and use a similar flow to 2A. 
Also, as a general rule any time you find yourself returning a tuple (multiple values) from a function it's a good sign that you need to break that function up. """

def is_valid_number(num: str): 
    try: 
        float(num) 
        return True
    except ValueError: 
        return False

def Rental_Cost():
    while True:
        dvd = input("Enter number of DVDs: ")
        if not is_valid_number(dvd):
            print("Invalid character(s) detected.")
        elif int(dvd) < 0:
            print("The number of DVDs must be a positive number.")
        else:
            dvd = int(dvd)
            break
            
    while True:
        vhs = input('Enter number of VHS tapes: ')
        if not is_valid_number(vhs):
            print("Invalid character(s) detected.")   
        elif int(vhs) < 0:
            print("The number of VHS tapes must be a positive number.")     
        else:
            vhs = int(vhs)
            break

    rental_cost = (3 * dvd) + (2 * vhs)
    return rental_cost, dvd, vhs

rental_cost, dvd, vhs = Rental_Cost()
print(f"\nThe total cost for {dvd} DVDs and {vhs} VHS tapes is ${rental_cost}.")
input('')
