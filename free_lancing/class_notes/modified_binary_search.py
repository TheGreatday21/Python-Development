
                                    #########BINARY SEARCH ONLY WORKS ON SORTED ARRAYS######
def find_first_occurrence(array,target):
    left = 0 
    right = len(array)-1
    first_occurrence = -1

    while left <= right:
        mid = (left + right)//2

        if array[mid] == target:
            first_occurrence = mid
            right = mid -1
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1   
    return first_occurrence

def find_last_occurrence (array, target):
    left  = 0
    right = len(array) -1
    last_occurrence = -1

    while left <= right:
        mid = (left + right)//2
        if array[mid] == target:
            last_occurrence = mid
            left = mid +1
        elif array[mid] < target :
            left = mid +1

def binary_search_all_occurrences(array, target):
    first = find_first_occurrence(array, target)
    last = find_last_occurrence(array,target)
    if first == -1:
        return []
    return list(range(first, last+1))

array= [1,1,1,2,2,3,3,4,5,6,6,6,6,6,6,7,8,9]
target = 3
result = binary_search_all_occurrences(array, target)


if result:
    print(f"Element found at indices{result}")
else:
    print("The element was not found")










