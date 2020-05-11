def get_initial(name, forced_uppercase=True):
    if forced_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input("Enter first name: ")
middle_name = input("Enter second name: ")
last_name = input("Enter last name: ")

print(f"The initals are: {get_initial(first_name)}{get_initial(middle_name)}{get_initial(last_name)}")