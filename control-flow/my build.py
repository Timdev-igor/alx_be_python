while True:
    select = input("What is the weather today (sunny, windy, or type 'exit' to quit): ").strip().lower()

    if select == "exit":
        print("Exiting the program. Stay safe!")
        break

    elif select == "sunny":
        try:
            degrees = int(input("How many degrees is it (30-47)?: "))
            if degrees == 40:
                print("The weather is moderately hot, wear sunglasses.")
            elif degrees <= 40:
                print(f"Sunny weather at {degrees} degrees is safe.")
            elif degrees > 49:
                print(f"High degrees like {degrees} are harmful for your skin.")
        except ValueError:
            print("Please enter a valid number for the temperature.")

    elif select == "windy":
        wind_speed = input("What is wind intensity (strong, mild)?: ").strip().lower()
        if wind_speed == "strong":
            print("It's windy in California. Choose options from below: BE SAFE")
            print("1. Wear a coat")
            print("2. Get indoors")
            choice = input("Choose an option (1 or 2): ").strip()
            if choice == "1":
                print("Can't wear this now.")
            elif choice == "2":
                print("Good, you chose the right option. Stay safe!")
            else:
                print("Choose a valid option.")

        elif wind_speed == "mild":
            print("It's windy in California. Choose options from below: BE SAFE")
            print("1. Wear a coat")
            print("2. Get indoors")
            choice = input("Choose an option (1 or 2): ").strip()
            if choice == "1":
                print("Thank you, the coat will protect you from the cold.")
            elif choice == "2":
                print("Good, stay safe. Still, you can go outside with a coat.")
            else:
                print("Choose a valid option.")

        else:
            print("Invalid wind intensity option. Please choose 'strong' or 'mild'.")

    else:
        print("Please choose from the provided options (sunny, windy, or exit).")
