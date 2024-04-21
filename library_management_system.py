class Library:
    def __init__(self) :
        self.no_book=0
        self.books=[]
    def addBooks(self,books):
        self.books.append(books)
        self.no_book = len(self.books)
        
    def showinfo(self):
        print(f"The no of books are {self.no_book}.They are : ")
        for book in self.books:
            print(book)
        
l1=Library()
l1.addBooks("Atomic Habit")
l1.addBooks("harry poter1")
l1.addBooks("Atomic Habit")
l1.addBooks("harry poter1")
l1.addBooks("Atomic Habit")
l1.addBooks("harry poter1")
l1.addBooks("Atomic Habit")
l1.addBooks("harry poter1")
l1.showinfo()