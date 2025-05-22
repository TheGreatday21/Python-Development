
def count():
    count_name = 0
    names_input = (input("Write any names here:"))
    names = list(names_input.split())
    for name in names:
        count_name +=1
        print(f"You have input {count_name} names in total")
    names = {}
    names_dictionary = names
    print(names_dictionary)
count()

