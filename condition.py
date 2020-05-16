# price = float(input("Enter the price of the product: "))

# if price >= 40.0:
#     tax = 0.1 * price
#     print(f"Total cost: {price + tax}")
# else:
#     print(price)

country = "Popricol"
if country.lower() == "popricol":
    print("You are a wierd one")
else:
    print("You are a normal one")
    
value = 16

#The use of 'elif'
if value <=15:
    print("The value is less than 15")
elif value <=30:
    print("The value is less than 30 and greater than 15")
elif value <=60:
    print("The value is less than 60 and greater than 30")
else:
    print("Greater than 60")

# The use of 'in'
name = "Gean"
if name.lower() in ("gean","rogers","po"):
    print("I know you")
else:
    print("I don't know you")

#The use of "and", "or"

packs = 5
tick = 1
if packs == 5 or packs == 7:
    print("This is very odd")
elif packs == 6 and tick == 1:
    print("This is great")

# use of not

if not (5 == 6): # or not 5 == 6
    print(True)