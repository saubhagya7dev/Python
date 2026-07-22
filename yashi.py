import math

# Add two no.
num1 = float(input("enter the first no."))
num2 = float(input("enter 2nd no."))
sum = num1 + num2
print("the sum of given no. is: ", sum)

# Calculate area of rectangle
length = int(input("Enter the length of rectangle: "))
breadth = int(input("Enter the breadth of rectangle: "))
area = length * breadth
print(area)


# interest calculator
principle = int(input("Enter the principal amount: "))
rate = int(input("Enter the rate of interest: "))
time = int(input("Enter the time period: "))
simple_interest = (principle * rate * time) / 100
amount = principle + simple_interest
print("Simple Interest:", simple_interest)
print("Total Amount:", amount)

# Square root of the given no.
num = int(input("Enter the no. to calculate the square root"))
sr = math.sqrt(num)
srmathformula = num ** (1 / 2)
print("square root of the given no. is: ", sr)

# Find the area of the triangle -
base = int(input("Enter the base of the triangle"))
height = int(input("Enter the Height of the Triangle"))
area = (1 / 2) * base * height
print("area of the triangle is : ", area)
