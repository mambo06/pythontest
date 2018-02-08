def factorial(n):
    factr = 1
    while (n >0):
        factr *= n
        n -= 1

def recursive_factorial(n):
   if n == 1 :
       return 1
   return n * recursive_factorial(n-1)

# print(recursive_factorial(5))

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)