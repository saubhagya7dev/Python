import math


# 1. Add two numbers
def add_two_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    total = num1 + num2

    print("The sum of the given numbers is:", total)


# 2. Calculate area of rectangle
def area_of_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))

    area = length * breadth

    print("The area of the rectangle is:", area)


# 3. Calculate Simple Interest
def calculate_simple_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period: "))

    simple_interest = (principal * rate * time) / 100
    amount = principal + simple_interest

    print("Simple Interest:", simple_interest)
    print("Total Amount:", amount)


# 4. Calculate square root
def calculate_square_root():
    num = float(input("Enter the number to calculate the square root: "))

    square_root = math.sqrt(num)

    print("The square root of the given number is:", square_root)


# 5. Calculate area of triangle
def area_of_triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))

    area = (1 / 2) * base * height

    print("The area of the triangle is:", area)


# 6. Swap two numbers
def swap_two_numbers():
    x = 13
    y = 10

    print("Before swapping:")
    print("x =", x)
    print("y =", y)

    # Python's shortcut for swapping
    x, y = y, x

    print("After swapping:")
    print("x =", x)
    print("y =", y)


# 7. Check if number is Odd or Even
def check_odd_even():
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")


# Main function
def main():
    add_two_numbers()
    print()

    area_of_rectangle()
    print()

    calculate_simple_interest()
    print()

    calculate_square_root()
    print()

    area_of_triangle()
    print()

    swap_two_numbers()
    print()

    check_odd_even()


# Call the main function
if __name__ == "__main__":
    main()
