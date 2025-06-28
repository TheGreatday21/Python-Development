def search(array,target) :
    for i in range (len(array)):
        if array[i] == target:
            return i
    return -1
data = [ 2,3,5,7,8,9]
new = 3

result  = search(data, new)

print(f"Your number {new} is at index {result}")
