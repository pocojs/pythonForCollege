class Library:
    def __init__(self, library):
       self.library = library
       self.books = []
        
    def __len__(self):
      return len(self.books)   
  
    def add_book(self, book):
        self.books.append(book)
        print(self.books)
    
    def remove_book(self, book):
        self.books.remove(book)      
        print(self.books)             
                       
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Название:{self.title},Автор:{self.author},Год:{self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"                
            
library = Library("My library") 
book1 = Book("Война и мир", "Лев Толстой", 1869) 
book2 = Book("Маленький принц", "Антуан де Сент-Экзюпери", 1943) 
book3 = Book("Мятная сказка", "Александр Полярный", 1994) 
library.add_book(book1) 
library.add_book(book2) 
library.add_book(book3) 
library.remove_book(book1)
print(len(library)) 