# Using predefined numbers
numbers = [6, 2, 4, 7, 9, 2]

# Calculating the sum
sum_result = sum(numbers)

# Calculating the product
product_result = 1
for num in numbers:
    product_result *= num

# Calculating the division (left to right)
division_result = numbers[0]
for num in numbers[1:]:
    if num != 0:
        division_result /= num
    else:
        division_result = "Division by zero is not allowed"
        break

# Displaying the results
print(f"Numbers: {numbers}")
print(f"Sum: {sum_result}")
print(f"Product: {product_result}")
print(f"Division: {division_result}")