#these are the same every way. The use key value pairs 


words = {
   "Harry" : "Gryfindoor",
   "Ron" : "Gryfindoor",
   "Draco" : "Slytherine",
   "Hermione" : "Gryfindoor"
}

#we can only see keys if we use the usual for loop way of doing things
for word in words:
    print(word)

#Here we are printing the keys of the dictionary and also the values using indexing .we index the dict words with the variable word 
for word in words:
    print(word, words[word] ,sep=" ,")

#printing the values in the dictionary 
for value in words.values():
    print(value)

#printing the keys in the dictionary 
for key in words.keys():
    print(key)



#in a case where we have more data to associate to a student 
#a nested dictionary in a list where the dictionaries have the same keys but unique values
students = [
    {"name":"Hermione", "house":"Gryfindoor", "patronus": "Otter"},
    {"name":"Ron", "house":"Gryfindoor", "patronus": "Jack russel carrier"},
    {"name":"Harry", "house":"Gryfindoor", "patronus": "Stag"},
    {"name":"Draco", "house":"Slytherine", "patronus": None}, #here we use the key word none to indicate that this hass no value at the end of  it 
]

#here using indexes we print all the values associated with the keys in the dictionary respective to each student in the dictionary 
for student in students:
    print(student["name"],student["house"],student["patronus"], sep=" , ")












