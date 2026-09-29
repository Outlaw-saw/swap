a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))

print(f"\nBefore swapping: a = {a}, b = {b}")

temp = a
a = b
b = temp

print(f"After swapping:  a = {a}, b = {b}")
