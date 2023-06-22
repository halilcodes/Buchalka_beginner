def is_palindrome(word:str):
    if type(word) is not str:
        return False
    word = word.lower().strip().replace(" ", "")
    return word[::-1] == word

""" print(is_palindrome("adc"))
print(is_palindrome("adcda"))
print(is_palindrome(123))
print(is_palindrome("adcdA")) """

def palindrome_sentence(sentence:str):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)

print(palindrome_sentence("Was it a car, or a cat. I saw?"))