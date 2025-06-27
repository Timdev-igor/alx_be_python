# static methd = mthd tht belongs to a class rathher than any objeect from that class
# used for general utility functions

# instance mths = best for operations on instances of the class (objects)
# static methods = Best for utility functions that do not  need access to class data


class Employee:

    def __init__(self,name ,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name}  = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["manager", "cook", "janitor", "cashier"]
        return position in valid_positions
    

employee1 =  Employee("Eugene" , "manager")
employee2 =  Employee("squid" , "cashier")

print(Employee.is_valid_position("cook"))
print(employee1.get_info())

# class mthds

class Student:
    count = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    def get_info(self):
        return f"{self.name} = {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total student {cls.count}"

student1 = Student("ponge", 3.5)
student2 = Student("pongesf", 3.8)
student3 = Student("preee", 4.0)


print(Student.get_count())