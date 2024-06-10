def fibonacci_recursive(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
   
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# fibonacci_recursive
print(fibonacci_recursive(0))  
print(fibonacci_recursive(1))  
print(fibonacci_recursive(5))  
print(fibonacci_recursive(10)) 
