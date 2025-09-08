#this is about strings and some of its built in functions

name = input("Whats your name ? ")

#this function removes white space from the string . The excess space we add when we enter text 
name= name.strip()
"""
Whats your name ?      dslhsdlahgddsahgdw
dslhsdlahgddsahgdw
"""
#the initialised white space from the user in the terminal is removed

#this function capitalises only the first letter  of the first word in a sentence 
caps = name.capitalize()
"""
Whats your name ? elijah the great
Elijah the great

"""

#this function capitalises every first letter of a word in the sentence 
headTitle = name.title()#very useful in name entry kind of thing 
"""
Whats your name ? elijah the great
Elijah The Great

"""

##### we can also chain all these methods onto the input function at once 
#name = input("Whats your name: ").strip().title()

#the split function takes args of what it starts splitting at and can assign the split values to variables on assignment as shown below 
first, last = name.split(" ") #when it sees blank space it will split the words at that point and place them into first and last respectively 


one = name[:3] #this takes the values from index 0 to 3 of the array ccontaining the string 

#print(name)
#print(caps)
#print(headTitle)
#print(one)
print(first," ",last)