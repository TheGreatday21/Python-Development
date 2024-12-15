 
                    #FIBONACCI SEQUENCE
'''
#METHOD 1
n = 10
num1 = 0
num2 = 1
next_number = num2  
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()


#METHOD 2

def fibonacci (n):
    i = 1
    a = 0
    b = 1
    list = []
    while i <= n:
        list.append(a)
        i += 1
        c = a + b
        a = b
        b = c
        
    print(f"The fibonacci series is {list}")

    print(f"The {n}th fibonacci number is {list[-1]}")
    
fibonacci(20)
'''
'''

                #TOWER OF HANOI

def T_O_H(n, source_rod, final_rod, middle_rod):

    if n == 1: #for only the first rod being moved 
        print(f"Move disk 1 from rod {source_rod} to  rod {final_rod}")
        return

    T_O_H(n-1, source_rod, middle_rod, final_rod)
    print(f"Move disk {n} from rod {source_rod} to rod {final_rod}")
    T_O_H(n-1,middle_rod,final_rod ,source_rod)

n = 3

T_O_H(n, "A","B","C")

'''
''''
        #FACTORIAL OF NTH NUMBER 
def factorial (n):
    i = 1
    

    while i <= n:
        
        i + 1
        n = n * i 
        return n

    return -1

n = 8
result  = factorial(n)

if result != -1:
    print(f"Your factorial of {n}  is {result}")
else:
    print("non operable")

'''
''''
            ##STACKS 

#this is  LIFO data structure 
n = 10
i = 1
stack = []
while i <= n:
    stack.append(i)
    i += 1
print(stack )




            #QUESES 

    
#Thesse are FIFO datastructures 

from collections import deque

my_queue = deque()

my_queue.append("keks")
my_queue.append("sdss")
my_queue.append("keksd")

print(my_queue)


popped = my_queue.popleft()

print(popped)
print(my_queue)

'''
''''
            ##QUIZES

#Write a Python function to calculate the sum of the first `n` natural numbers using a loop. Analyze the time complexity of your solution.  


def sum_nn (n):

    list_n = []
    sum = 0

    for i in range(1, n+1):
        sum += i
        list_n.append(i)
        print(list_n)
    return sum
n = 10


print(sum_nn(n))



def toh(n, s_n , f_n , m_n):

    if n == 1:
        print(f"Move disk {n} from {s_n} to {f_n} ")
        return
    toh(n-1, s_n, m_n , f_n)
    print(f"Move disk {n} from {s_n} to {f_n}")
    toh(n-1, m_n, f_n, s_n)

toh(3, "F","G","H")



def b_search(Array,target):
    left = 0
    right = len(Array) -1
    comparisons = 0

    while left <= right:
        mid = (left + right) //2
        comparisons += 1
        if Array[mid] < target:
            left = mid + 1
        elif Array[mid] > target:
            right = mid - 1
        else:
            print(f"Got the answer in {comparisons} comparisons")
            return mid
    return -1



Array = [2,3,5,7,8]

target = 7


result  = b_search(Array,target)
if  result != -1:
    print(f"The target is at index {result} in  ")
else:
    print("The target is not in the sorted list ")


def factorial(n):
    """
    Calculates the factorial of a given number recursively.

    Args:
        n: The number for which to calculate the factorial.

    Returns:
        The factorial of n.
    """
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n-1)  
print(factorial(4))


'''

def bubble(nums):
    for i in range(len(nums)- 1, 0 , -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j +1]
                nums[j+1] = temp


nums = [ 2,3,9,1,6,4]

bubble(nums)

print(nums)