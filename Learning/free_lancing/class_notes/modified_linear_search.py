def linear_search_modified(array,target):
    indices = []
    for i in range(len(array)):
        if array[i]==target:
            indices.append(i)
    return indices

array = [1,2,4,4,8,7,0,5,0,3,6,9,]
target = 4
result = linear_search_modified(array,target)

if result:
    print(f"Elements found at indices {result}")
else:
    print("Element not found")





