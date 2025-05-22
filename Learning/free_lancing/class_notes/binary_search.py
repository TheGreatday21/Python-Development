def binary_search(array,target):
    left=0
    right=len(array)-1

    while left<=right:
        mid=(left+right)//2

        if array[mid] == target:
            return mid
        elif array[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

  
array = [3,7,8,4,2,1,6,8,9]
target = 10
result=binary_search(array,target)

if result!= -1:
    print(f"Element {target} is at index {result} of list {array}")
else:
    print("Element not found")    
