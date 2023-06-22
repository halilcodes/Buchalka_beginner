com_parts = {"1": "computer", "2": "monitor", "3": "keyboard", "4": "mouse", "5": "mouse mat"}


def deep_copy(original: dict) -> dict:
    return {key: value for key, value in com_parts.items()}


com_copy = deep_copy(com_parts)
print(id(com_copy))
print(id(com_parts))
