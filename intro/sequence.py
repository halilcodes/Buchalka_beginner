shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# another_list = shopping_list.copy()
another_list = shopping_list

print(id(shopping_list))
print(id(another_list))
print(another_list)
print(shopping_list)

shopping_list += ["cookies"]
print(id(shopping_list))
print(id(another_list))
print(another_list)
print(shopping_list)

a = b = another_list
a.append("cream")
print(id((a)))
print(b)
print(id((b)))
print(shopping_list)