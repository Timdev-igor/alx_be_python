size = int(input("Enter the size of the pattern: "))

if size > 0:
    row = 0
    while row < size:
        print("*" * size)  # Print a row of asterisks
        row += 1
else:
    print("Please enter a positive integer for the pattern size.")
