names = ["John","Steve","Stacy"]

name   = input("What is your name : ")

for n in names:
    if name == n:
        print("Found")
        break
else:# wew can also use else statements with for loops . If we donot break out of the loop we can run the else block 
    print("Not found ")

# we can also use 
if name  in names:
    print("Found")
else:
    print("Not found")


####DICTIONARIES 

#a list of dictionariess 
people = [
    {"name":"Elijah", "number": "0787106109"},
    {"name":"Liah", "number": "0712804279"},
    {"name":"Johanes", "number": "0729017422"}
]

userName = input("name: ")

for person in people:
    if person["name"] == userName:
        number = person["number"]
        print(f"Found {number}")
        break
else:
    print(f"{userName} Not Found")























