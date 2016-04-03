# "eat your own dog food; using this instead of built-in reversed"
from reverse_string import reverse_string


def is_palindrome(string):
    if not string:
        return False

    return all(string[i].upper() == x.upper() for i, x in enumerate(reverse_string(string)))

if __name__ == "__main__":
    while True:
        print("Please input a string to see if it is a palindrome. Press enter without entering anything else to exit.")
        val = input()
        if not val:
            break

        print(is_palindrome(val))
