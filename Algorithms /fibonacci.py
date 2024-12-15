 
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
'''

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
