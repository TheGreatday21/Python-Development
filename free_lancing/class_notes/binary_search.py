def binary_search(array,target):
    left=0
    right=len(array)-1
    while left<=right:
        mid=(left+right)//2
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

  
array = [3,7,8,4,2,1,6,9]
target = 9
result=binary_search(array,target)

if result!= -1:
    print(f"Element is at index {result}")
else:
    print("Element not found")    
