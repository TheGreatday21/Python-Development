class Book:
  def __init__(self,title,author,copies_available):
    self.title = title
    self.author = author
    self.copies_available = copies_available
    
  def borrow_book(self,book_name):
    if self.copies_available > 0:
      if self.title == book_name:
        self.copies_available -= 1
        print(f"You have borrowed a copy of {self.title}, copies left: {self.copies_available}")
      else:
        print("Book not available")
    else:
      print("There are currently no copies to borrow")
      
  def return_book(self,book_name):
    if self.title == book_name:
      self.copies_available += 1
      #book count keeps track of all the borrowed books
      print(f"You have returned a copy of {self.title}, copies left: {self.copies_available}")
    else:
      print("Book not available")


def main():
  #instance of the book class
  book1 = Book("Goosebumps","RL Stein",40) 
  book1.copies_available = 50# changed copies available to 50
  book2 = Book("Harry Potter", "Jk Rollin", 5)
  
  book2.borrow_book("Harry Potter")
  #this shows us we have borrowed one copy of the book and copies left
  book2.borrow_book("The Flash")
  #output shows the book is not available
  
  # demonstrating borrowing  until depletion using a loop 
  for _ in range(5):
    book2.borrow_book("Harry Potter")

  # returning a copy 
  book2.return_book("Harry Potter")
  #borrowing again to show depletion of books works 
  book2.borrow_book("Harry Potter")
  
if __name__ == "__main__":
    main()