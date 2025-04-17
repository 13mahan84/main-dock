

# Getting 6 numbers from the user
numbers = []
for i in range(6):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculating the sum
sum_result = sum(numbers)

# Calculating the product
product_result = 1
for num in numbers:
    product_result *= num

# Calculating the division (starting from the first number)
division_result = numbers[0]
for num in numbers[1:]:
    if num != 0:
        division_result /= num
    else:
        division_result = "Division by zero is not allowed"
        break

# Displaying the results
print(f"Sum: {sum_result}")
print(f"Product: {product_result}")
print(f"Division: {division_result}")

Let me know if you'd like it as a function or with a GUI!

