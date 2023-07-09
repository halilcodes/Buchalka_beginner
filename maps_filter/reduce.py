import functools


def calc_values(x, y: int):
    print("x: ", x, "y: ", y)
    return x * y


numbers = [2, 3, 5, 8, 13]

record_value = functools.reduce(calc_values, numbers)
print(record_value)
print(sum(numbers))


