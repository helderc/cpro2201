
class Book:
    def __init__(self, title, author="NA"):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f"You borrowed: {self.title}")
        else:
            print("The book is not available!")
    
    def return_book(self):
        self.available = True
        print(f"Your returned: {self.title}")
        
    def is_available(self):
        if self.available:
            return True
        return False
    
class Store:
    def __init__(self):
        self.my_book = Book()
    
#
b1 = Book("Life of Pi", "Author...")
print(f"B1: {b1.title}, {b1.author}")
b1.borrow()
b1.borrow()
b1.return_book()
b1.borrow()

b2 = Book("The Book of Why")
print(f"B2: {b2.title}, {b2.author}")

books = [b1, b2]

for b in books:
    print(f"> {b.title}; {b.author}; {b.is_available()}")

all_titles = [ b.title for b in books ]

#%%
print(type(b1))

b1.info = "information"
print(b1.info)












