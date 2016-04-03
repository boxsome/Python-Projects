def reverse_string(string):
    return string[::-1]

if __name__ == "__main__":
    while True:
        print("Please input a string to see its reversed. Press enter without entering anything else to exit.")
        val = input()
        if not val:
            break

        print(reverse_string(val))
