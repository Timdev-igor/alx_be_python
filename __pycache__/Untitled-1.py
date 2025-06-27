class Books :
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    
    def __del__(self):
        print (f"{self.title} has been deleted")
    
    def __str__(self):
        return f"A book {self.title} ,by {self.author}in {self.year}"
    def __repr__(self):
        return f"A book {self.title} ,by {self.author}in {self.year}"
    
book1 = Books("1984", "George Orwell", 1949)
print(book1)      # Calls __str__
print(repr(book1))  # Calls __repr__

del book1 
