import math

x = 5


def foo(y):
    # global x
    x = y
    print(x)
    print(y)


print("-----------")
print(x)

print("----------")
foo(6)

print("----------")
print(x)