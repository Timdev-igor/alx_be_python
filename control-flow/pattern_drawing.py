size = int(input("Enter the size of the pattern: "))

# Check if the input is a positive integer
if size > 0:
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")  # Print asterisk without newline
        print()  # Print newline after each row
        row += 1
else:
    print("Please enter a valid positive integer for the pattern size.")
