weather = input("what is the fucking weather today? :  ")

if weather == "sunny":
   print("you dumbass , get sunscreen")
elif weather == "windy":
   print("nigga get the hell inside a house")
elif weather == "rainy":
   print("get a gaddamn umbrella befor you get all wet dumbass")
else:
   num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using match case
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation.")