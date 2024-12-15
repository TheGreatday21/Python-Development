#PRACTICING MY ALGORITHMS 
''''

## FIBONACI NUMBER 
def fibonacci():
    a = 0
    b = 1
    c = a + b
    for i in range(0,10):
      


##SORTING ALGORITHMS

                #simple implementations 
#1.
unsorted_list = [14,27,8,-42,11,35,-9,56,23]

unsorted_list.sort()

print (unsorted_list)

#2.
unsorted_list_1 = [14,27,8,-42,11,35,-9,56,23]

sorted_list = sorted(unsorted_list_1)

print (sorted_list)

#3.
#printing it in reverse order using the reverse 
unsorted_list = [14,27,8,-42,11,35,-9,56,23]

unsorted_list.sort(reverse=True)

print(unsorted_list)
'''

'''
            ##### BUBBLE SORT 
#to import arrays there is a type code you need to know inorder to have the write integers showing 
#- i for all positive and negative integers but not floats 
#- I for only positive integers 


#arrays are not default so we call the library 
from array import *
#here we create the array
unsorted_array = array("i",[14,27,8,-42,11,35,-9,56,23]) 

def bubble_sort(array):

    for i in array:
        i = 0
        i < array.length - 1
        i =+ 1
        
        print(i)

bubble_sort(unsorted_array)

'''

''''         ##BINARY SEARCH
#only works on sorted lists
list = [1,2,3,4,5]
target = 3

def  bin_search(list,target):
    
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right)/2

        if list[mid] == target:
            return (mid)
        elif list[mid] < target:
            left = mid + 1
        elif list[mid] > target:
            right = mid - 1
    return -1

bin_search(list, target)
'''


from array import *

keks = array("i",[3,4,1,8,9])

for i in range(len(keks)):
   print(keks[i])

##unique method of printing all the values in the array
for e in  keks:
   print(e)

























