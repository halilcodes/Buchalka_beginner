entries = [1, 2, 3, 4, 5]
print("entries")
print(f"all: {all(entries)}")
print(f"any: {any(entries)}")
print("*" * 40)
another = [0, False, None, ""]
print("another")
print(f"all: {all(another)}")
print(f"any: {any(another)}")
print("*" * 40)

the_other = [0, 1, False, ""]
print("the_other")
print(f"all: {all(the_other)}")
print(f"any: {any(the_other)}")
print("*" * 40)
