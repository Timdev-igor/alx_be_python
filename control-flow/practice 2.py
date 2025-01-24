class student:
    student_count = 0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.student_count += 1

    def show(self):
        return f"Name:{self.name} Age: {self.age}"
    
    @classmethod
    def count_students(cls):
        if cls.student_count == 1:
             return f"There is  {cls.student_count} student now"
        elif cls.student_count > 1:
            return f"There  are {cls.student_count} students now"
        else:
            return "invalid"

    
obj1 = student("Alma",17)
obj2 = student("Alsa",16)
print(obj1.show())
print(student.count_students()) 



        

        

       