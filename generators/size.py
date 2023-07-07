import sys


def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print(f"my_range while yielding {start}")
        yield start
        start += 1


# big_range = range(1000)
big_range = my_range(5)

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

big_list = [val for val in big_range]

print("big_list {} bytes".format(sys.getsizeof(big_list)))

print(big_range)

print(big_list)
