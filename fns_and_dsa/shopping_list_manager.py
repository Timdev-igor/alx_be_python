def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # put an empty list 

    while True:
        display_menu()  # Display the menu to the user
        choice = input("Enter your choice: ")  # Get user input

        if choice == '1':
            # Add an item to the shopping list
            item = input("Enter the item you want to add: ")
            shopping_list.append(item)  # Add item 
            print(f"'{item}' has been added to your shopping list.")

        elif choice == '2':
            # Remove an item from list
            item = input("Enter the item you want to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)  # Remove the item 
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in your shopping list.")

        elif choice == '3':
            # View shopping list
            if shopping_list:
                print("Your Shopping List:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is currently empty.")

        elif choice == '4':
            # Exit
            print("Goodbye!")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()