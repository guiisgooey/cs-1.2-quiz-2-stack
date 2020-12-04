word = input("Enter a word to reverse: ")
stack = []

def reverse_string(word):
    """reverses string using the properties of a stack"""
    n = len(word)
    for i in range(n):
        stack.append(word[i])
    new_word = ""
    for i in range(n):
        new_word += stack.pop()
    return new_word

new_word = reverse_string(word)
print(f"Your original word: {word}")
print(f"Your reversed word: {new_word}")