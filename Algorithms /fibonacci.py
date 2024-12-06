def fibonacci(n):
    
    if (n <= 1):
        return n 
    return fibonacci(n-1)+ fibonacci(n-2)
    
n = 5
result = fibonacci(3)

print(f"The fibonacci number is {result}")