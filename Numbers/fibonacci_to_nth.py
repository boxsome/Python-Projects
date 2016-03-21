# **Fibonacci Sequence** - Enter a number and have the program generate the Fibonacci
# sequence to that number or to the Nth number.
# Uses a generator to generate fibonacci sequence up to the n-th digit
# Space: O(1) excluding the returned list
# Time: O(n) to generate the entire sequence


def _fibonacci_generator(n):
    """Generates fibonacci numbers in sequential order"""
    a, b = 0, 1
    for _ in range(1, n+1):
        yield a
        a, b = b, a+b


def fibonacci_to_nth(n):
    """Function takes an int *n* and outputs the fibonacci sequence up to and including the n-th fibonacci number."""
    if not isinstance(n, int):
        raise TypeError("Input 'n' must be of type int.")
    elif n < 0:
        raise ValueError("Input 'n' must be a non-negative integer")

    return [num for num in _fibonacci_generator(n)]

if __name__ == "__main__":
    print("Please enter up to how many numbers from the fibonacci sequence you would like to have:")
    print(fibonacci_to_nth(int(input())))