def linear_search(array,target):#Array is fo rthe elements present and the target is the element we are looking for in the array#
	for i in range(len(array)): 
		if array[i] == target:
			return i
	return -1 #standard way of saying e=what you looked for doesnt exist #
data = [ 3,2,5,7,8,1]
target = 8
result = linear_search(data, target)
if result !=-1:
	print(f"the element is at index {result}")
else:
	print("the element was not found")