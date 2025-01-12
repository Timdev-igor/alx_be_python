from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    # Format the current date and time in "YYYY-MM-DD HH:MM:SS" format
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

# Part 2: Calculate a Future Date
def calculate_future_date(days_to_add):
    # Get current date
    current_date = datetime.now()
    # Add days using timedelta
    future_date = current_date + timedelta(days=days_to_add)
    # Print the future date in "YYYY-MM-DD" format
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

# Main function
def main():
    # Part 1: Display the current date and time
    display_current_datetime()
    
    # Part 2: Get user input for the number of days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Call the function to calculate and display the future date
        calculate_future_date(days_to_add)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()
