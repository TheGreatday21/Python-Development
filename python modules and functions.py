''''
###Handling text in pythom
# r - read
# w is write
# r+ is read and write
# x is create
# a is append
## we use the with open statement
text = "Hellooooo\n My name is Kaizzi Elijah the great bashi\n Wasap my niggas \n"
with open("keks.txt",'w') as file:
    file.write(text)
    #we have successfully created the text file called keks
# to append to it
text = "Damn what a loveley day"
with open("keks.txt",'a') as file:
    file.write(text)


##note
###incase your file is on the desktop you have to usee \\ when stating its file path .. this is the escape sequence 

#example 1
with open("keks.txt","r") as file:
    print(file.read())

##getting the file from a desktop we only use  a forward slash
with open("/Users/keksmacbookair/Desktop/keks2love.docx","r") as file:
    print(file.read())

'''



