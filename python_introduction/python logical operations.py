# logical operations (or / and / not)
# or = at least one condition must be True
# and = both conditions true
# not = invertse the condition

temp = float(input("Enter the temperture: "))

# 'or' operation
"""
is_snowing = False

if temp > 45 or temp < 0 or is_snowing :
    print("You cant go outside")
else :
    print("you can go outside")

"""
# 'and' operation
is_sunny = False

if temp >= 28 and is_sunny :
    print("its hot outside")
    print("its sunny")
elif temp <= 0 and is_sunny:
    print("its cold outside")
    print("its sunny")
elif 28 > temp >  0 and is_sunny:
    print("its  moderate  outside")
    print("its sunny")

# not function used  below -------------

elif temp >= 28 and not is_sunny :
    print("its hot outside")
    print("its cloudy")
elif temp <= 0 and is_sunny:
    print("its cold outside")
    print("its cloudy breezy")
elif 28 > temp >  0 and not is_sunny:
    print("its  moderate  outside")
    print("its cloudy warm ")