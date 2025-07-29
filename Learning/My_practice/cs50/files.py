#python has built in support for csv files 
import csv

file = open("phonebook.csv" , "a") #opeining it in append mode 

name  = input("Name: ")
number = input('Number: ')

#putting the name and number into the file 
writer = csv.writer(file)#open the file and be ready to write to it 
writer.writerow([name,number])
##writer is a really helpful function that helps us write to files 
file.close()




# we can also open files using the with functino thats more efficient
# the code could have been 

with open("phonebook.csv","a") as file:
    writer2 = csv.DictWriter(file, fieldnames=["name","number"])
    writer2.writerow({"name":name, "number":number})

















































