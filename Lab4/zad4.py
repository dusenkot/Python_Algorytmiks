
def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
    

def fibonacci_iterative(n):
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci_recursion(10))
