com_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]
choice = "-"
shop_list = []

while choice != "e":
    if choice in "01234":
        shop_list.append(com_parts[int(choice)])
        print(f"Adding {com_parts[int(choice)]}")
    else:
        print("Add options from the list below:")
        for i, part in enumerate(com_parts):
            print(f"{i}: {part}")
        print("e: to exit")
    choice = input("Select: ")

# print(f"Your list contains {*shop_list}")
print(shop_list)