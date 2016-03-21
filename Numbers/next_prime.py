# **Next Prime Number** - Have the program find prime numbers until the user chooses to stop asking for the next one.


def next_prime():
    """Generator that returns prime numbers in sequential order."""
    yield 2
    prime_num = 3
    prev_primes = []

    while True:
        yield prime_num
        prev_primes.append(prime_num)

        while True:
            prime_num += 2
            if all(prime_num % i != 0 for i in prev_primes):
                break

if __name__ == "__main__":
    prime_iter = next_prime()
    while True:
        print("Current prime number: " + str(next(prime_iter)))
        get_next = input("Get next prime number? (y or n): ")
        if get_next != "y":
            break
