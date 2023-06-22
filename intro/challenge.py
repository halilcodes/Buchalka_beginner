user_nums = input(" Please enter three numbers: ")

print(type(user_nums))
numbers= user_nums.split(",")

print(sum([int(i) for i in numbers]))