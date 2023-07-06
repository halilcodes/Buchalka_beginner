import sys

big_range = range(1000)

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

big_list = [val for val in big_range]

print("big_list {} bytes".format(sys.getsizeof(big_list)))

