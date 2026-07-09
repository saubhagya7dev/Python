# Calculate area of rectangle

l = int(input("Enter the length of rectangle: "))
b = int(input("Enter the breadth of rectangle: "))
area = l * b
print(area)


# interest calculator
principle = int(input("Enter the principal amount: "))
rate = int(input("Enter the rate of interest: "))
time = int(input("Enter the time period: "))
simple_interest = (principle * rate * time) / 100
amount = principle + simple_interest
print("Simple Interest:", simple_interest)
print("Total Amount:", amount)
