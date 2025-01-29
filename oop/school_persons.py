""" this is a practice on using __str__ , single_inheritance and __repr__ and delete"""
class  person:


    def __init__(self,person_name, person_age):
        self.person_name=person_name
        self.person_age=person_age
    
    def delete(self):
        """Custom method to delete an object manually"""
        print(f"Deleting {self.__class__.__name__}: {self.person_name}")
        del self  #

    
class  student(person):
    def __init__(self,person_name,person_age,student_class):
        super().__init__(person_name, person_age)
        self.student_class=student_class

        """using strings and reps"""
    
    def __str__ (self):
       return  f"student: {self.person_name}  Age :{self.person_age}  class/form: {self.student_class}"
    
    def __repr__(self):
        return f"Student('{self.person_name}', {self.person_age}, '{self.student_class}')"
         
         
class teacher(person):
    def __init__(self, person_name, person_age,teacher_subject):
        super().__init__(person_name, person_age)
        self.teacher_subject=teacher_subject

        """using strings and reps"""
    
    def __str__ (self):
        return  f"Teacher: {self.person_name} Age:{self.person_age} Subjects//:{self.teacher_subject}"
    
    def __repr__(self):
        return f"Teacher('{self.person_name}', {self.person_age}, '{self.teacher_subject}')"
  
    
class staff(person):
    def __init__(self, person_name, person_age,staff_profession):
        super().__init__(person_name, person_age)
        self.staff_profession=staff_profession

    """using strings and reps"""

    def __str__ (self):
        return  f"Staffname:{self.person_name}, profession:{self.staff_profession}"
    
    def __repr__(self):
        return f"Staff('{self.person_name}', {self.person_age}, '{self.staff_profession}')"

student1 = student("Alice", 15, "10A")
teacher1 = teacher("Mr. John", 40, "Mathematics")
staff1 = staff("Mrs. Smith", 50, "Office Manager")
staff2 = staff("Mr. Brown", 45, "Janitor")
staff3 = staff("Ms. Green", 38, "Librarian")
staff4 = staff("Dr. White", 60, "Administrator")
staff5 = staff("Mr. Black", 55, "Security Officer")


print(staff2)
print(staff3)
print(staff4)
print(staff5)


print(student1)
print(teacher1)
print(staff1)
student1.delete()


 




