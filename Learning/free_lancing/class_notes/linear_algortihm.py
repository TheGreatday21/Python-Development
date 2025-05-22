def linear_search(array,target):#Array is for the elements present and the target is the element we are looking for in the array#
	for i in range(len(array)): 
		if array[i] == target:
			return i
	return -1 #standard way of saying what you looked for does not exist #
data = [ 3,2,5,7,8,1]
target = 8
result = linear_search(data, target)
#Putting if statements for the result we are to get
if result != -1:
	print(f"The element is at index {result}")
else:
	print("The element was not found")