#this is a python script about lists in python 
def main():
    food = ["Rice", "Matooke","Pork","Irish"]

    for f in food:
        print(f)
    for i in range(len(food)): #Getting the number of items in the list using the len function
        #this is doing things dynamically 
        print(food[i], end="/--/") 

    #we can also have a list of dictionaries
    books = [
        {"name":"Harry Potter","pages":2333,"type":"fiction"},
        {"name":"Atomic Habbits","pages":766,"type":"discipline"},
        {"name":"The Hobbit","pages":5663,"type":"adventure"},
        {"name":"Fifty shades of Grey","pages":464,"type":"romance"}
    ]

    for book in books:
        print("\n")
        print(book["name"],book["pages"],book["type"], sep=" \/ ")
    
main()






