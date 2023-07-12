anon = lambda x: x * 2


def double(x):
    return x * 2
# both are same


print(anon)
print(double)

print(anon(7))
print(double(7))
print("*" * 40)

limit = 100
result = "in range" if limit < 100 else "equal" if limit == 100 else "out of range"
print(result)
print("*" * 40)


