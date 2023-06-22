com_parts = {"1": "computer", "2": "monitor", "3": "keyboard", "4": "mouse", "5": "mouse mat"}

current_choice = None
cart = []

while current_choice != "0":
    print("Add options from the list below: ")
    for key, value in com_parts.items():
        print(f"{key}: {value}")
    print("0: exit")
    current_choice = input("Select: ")
    if current_choice in com_parts:
        print(f"Adding {com_parts[current_choice]}...")
        cart.append(com_parts[current_choice])
    elif current_choice.casefold() in com_parts.values():
        print(f"Adding {current_choice}...")
        cart.append(current_choice)
print(cart)

