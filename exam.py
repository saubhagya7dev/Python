def multiple(num):
    for i in range(1, num + 1):  # Loop through possible values of i
        for j in range(1, num + 1):  # Loop through possible values of j
            if i * j == num:  # Check if the product equals num
                return i, j
    return "No two numbers can multiply to give the input number"

num = int(input("Enter a number: "))  # Get input from the user
result = multiple(num)  # Call the function with the input number
print(result)  # Print the result