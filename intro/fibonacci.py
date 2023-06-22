# 1 1 2 3 5 8

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return False
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(9))