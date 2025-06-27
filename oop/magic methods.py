#magic methods / dunder mthd  __mthd__ /cutomize behavior of objects

class Book:

    def __init__(self,title,author, num_page):
        self.author = author
        self.title = title
        self.num_page = num_page

    def __add__(self , other):
        return self.title + other
    
    def __str__(self):
        return f" {self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__ (self , other):    
        return  self.num_page < other.num_page
    
    def __add__ (self,other):
        return self.num_page + other.num_page
    
    def __contains__(self , keyword):
        return keyword in self.title
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_page
        else:
            return f"the {key} not found"


        
        

book1 = Book("death stranding" , "kojima",400)
book2 = Book("death stranding" , "kojima",410)
book3 = Book("death stranding 2 :on the beach" ,"kojima",420)


print(book1 == book2)
print(book1 == book3)
print(book2 < book3)
print(book1 + book3)

print("death " in book3)
print(book3["title"])


print(book1)