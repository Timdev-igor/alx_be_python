class Animal:
  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def make_sound(self):
    print("Woof!")

animals = [Dog(), Animal()]
for Dog in animals:
  Dog.make_sound()  # Output: Woof! (for Dog), Generic animal sound (for Animal)
