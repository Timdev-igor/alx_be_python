
class Car:
    # Class variable
    metre_reading = 10  # initial speed in km/hr

    def __init__(self, name, build, year):
        # Initialize instance variables
        self.name = name
        self.build = build
        self.year = year

    def show_details(self):
        # Return full details of the car
        full_details = f'Name: {self.name}, Build: {self.build}, Year: {self.year}'
        return full_details

    def read_metre(self):
        # Print the current meter reading
        print(f"This car has {Car.metre_reading} km/hr")

    def update_metre(self, mileage):
        # Update the meter reading only if the new mileage is greater
        if mileage >= Car.metre_reading:
            Car.metre_reading = mileage
        else:
            print("You can't roll back the meter!")

    def increase_metre(self, miles):
        # Increase the meter reading by a specified number of miles
        Car.metre_reading += miles


# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Show car details
print(my_car.show_details())

# Read initial meter reading
my_car.read_metre()

# Update the meter reading
my_car.update_metre(50)

# Read updated meter reading
my_car.read_metre()

# Increase the meter reading
my_car.increase_metre(15)

# Read final meter reading
my_car.read_metre()
