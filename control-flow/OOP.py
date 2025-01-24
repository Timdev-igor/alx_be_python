class Dog:  
        # class variable   
        count=0 #initial count of dogs before input , relates to line "9" and 15-18 and execution on line 24
        def __init__(self, name, bark ,year):  
            # Instance variable  
            self.name = name  
            self.bark = bark 
            self.year = year
            Dog.count += 1 
      
        # instance method to access instance variable  
        def show(self):  
           full_details =  f'Name: {self.name}, Bark: {self.bark}, Year: {self.year}'
           return full_details
      
        @classmethod
        def count_dogs(cls):
              # Class method to return the current count of dogs
            print(f"Total number of dogs: {cls.count}")
      
obj = Dog('Cmax', 'woof','2024') 
obj2 = Dog('rufus', 'ruff','2012') 

print(obj.show())
Dog.count_dogs()

        
        
