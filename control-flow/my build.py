select = str(input("what is the weather today(sunny,windy):? "))

match select :

    case 'sunny':
        degrees = int(input("how degrees is it(30-47)?:  "))
        if degrees ==  40:
            print("The weather is moderately hot ,wear sunglasses")
        elif degrees <= 40:
            print(f"Sunny weather at {degrees}degrees is safe.")
        elif degrees > 45:
            print(f"High deegrees like {degrees} are harmful for your skin ") 
    case 'windy':
        wind_speed = str(input("what is wind intensity(strong,mild):  "))
        if wind_speed == "strong":
            print("its windy in carlifornia choose options from below :BE SAFE")
            print("1. coat")
            print("4. get indoors")
            choice =str(input(":"))
            if choice == "coat":
                print("cant wear this now")
            elif  choice == "get indoors":
                   print("Good, you choose the right option,stay safe")
            else:
                   print("choose a valid option")
        elif wind_speed == "mild":
            print("its windy in carlifornia choose options from below :BE SAFE")
            print("1. coat")
            print("4. get indoors")
            choice =str(input(":"))
            if choice == "coat":
                print("Thank you, the coat will protect you from cold")
            elif  choice == "get indoors":
                   print("Good,stay safe, still you can go outside with a coat")
            else:
                   print("choose a valid option")
        else:
             print("invalid option")
    case _:
          print("please choose from the provided options in parenthesis")
             
   
        



        