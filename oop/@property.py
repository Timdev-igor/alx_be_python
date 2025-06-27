class rectangle:
    def __init__(self,width,length):
        self._length = length
        self._width = width
    @property
    def width(self):
        return f"{self._width:.1f} cm"

    @property
    def length(self):
        return f" {self._length:.1f} cm"
    
    @width.setter
    def width(self , new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("naah greater than 0")

    @length.setter
    def length(self , new_length):
        if new_length > 0:
            self._width = new_length
        else:
            print("naah greater than 0")
    
    @width.deleter
    def width(self):
        del self._width
        print("width deleted")
    @length.deleter
    def length(self):
        del self._length
        print("length deleted")

        

rect = rectangle(3,4)

rect.width = 5
rect.length = 6



print(rect.width)
print(rect.length)
del rect.width
