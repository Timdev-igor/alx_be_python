# Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table
for num in range(1, 11):
    product = number * num
    print(f"{number} * {num} = {product}")