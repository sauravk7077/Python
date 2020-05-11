from datetime import datetime

#Function to print current date and time
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

def get_initial(name):
    inital = name[0:1].upper()
    return inital

print("Hello")
print_time("Said Hello")

for n in range(0,11):
    print(n)
print_time("Counted Numbers")

first_name = input("First name: ")
last_name = input("Last name: ")

print(f"Your initials are: {get_initial(first_name)}{get_initial(last_name)}")



