x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

print()
try:
    print(x/y)
except ZeroDivisionError as e:
    print("Cannot divide by 0.")
else:
    print("Something else went wrong.")
finally:
    print("This is our cleanup.")
print()