## A collection is a single variable used to store multiple values
##collections branch of into :-
#lists = [] ordered and changeable. Duplicates okay
#Sets = {} unorderedand immutable. but Add/Remove okay . No duplicates
#Tuple = () ordered and unchanged Duplicates okay , faster 


#########using lists
fruits = ["apple", "pear", "Banana" , "Coconut" , "Melon"]
#apple is therefore our index 0 and to call it we print the variable with the indexin box brackets
print(fruits[0])
#To call more than one item /element from the list we provide an index range
print(fruits[0:3])
###Double :: is to tell python you want to make a step
##fo example a step backward is [::-1] and a step for  every  two numbers staring from index 0 [::2]
print(fruits[::-1])#for bckwards
print(fruits[::2])#for a two step count from index 0

###We can also iterate over our list using for loops
for fruit in fruits:
    print(f"\n\n{fruit}")

###There are a couple of functions we can use when working on our  list ..we can call them using the dir function
print(dir(fruits))
print(help(fruits))##description of all theattributes
##['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
##all the above are functions that can be used in alphabetical order
































