class Book:
    def __init__(self,title,author,year,price):
        self.title = title
        self.author = author
        self.year= year 
        self.price = price
        
    def discount(self):
        if  self.price >= 10000:
            d_sum = self.price * (10/100)
            self.price -= d_sum
            print(f"Discount: {d_sum} newprice: {self.price}")
            
        else:
            d_sum = self.price * (2/100)
            self.price -= d_sum
            print(f"Discount: {d_sum} newprice: {self.price}")
             
def main():

    me1 = Book("lido","DC",1998,15000)
    
    me1.price = 40000
    
    me1.discount()
        
if __name__ == "__main__":
    main()