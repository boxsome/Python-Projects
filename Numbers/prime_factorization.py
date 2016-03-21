# **Prime Factorization** - Have the user enter a number and find all Prime Factors (if there are any) and display them.
from enum import Enum
import math


# Class representing a prime factorization of an integer. Have the ability to define different algorithms to use
# to find the prime factorization of a given value
class PrimeFactorization(object):
    """Class that allows a user to get the prime factors of an integer
        For simplicity, we will only be considering positive integers.

    Attributes:
        n: Int to get prime factors for
    """

    def __init__(self, n):
        """Return PrimeFactorization object with value n and initialize prime factors list"""
        if not isinstance(n, int):
            raise TypeError("*n* must be of type int.")
        elif n < 0:
            raise ValueError("*n* must be non-negative int.")

        self.n = n
        self.__prime_factors = None
        self.__primes = {}

    # Enum for types of algorithm used to get the prime factors: allows us to expand in the future
    Algorithm = Enum("Algorithm", "trial_division")

    def get_prime_factors(self, algorithm = Algorithm.trial_division):
        """Gets the prime factors of self.n using the *algorithm* specified"""
        if self.__prime_factors is None:
            self.__prime_factors = set()

            if algorithm == PrimeFactorization.Algorithm.trial_division:
                self._trial_division()

        return self.__prime_factors

    def _trial_division(self):
        """Gets the prime factors of self.n using trial division"""
        upper_bound = math.ceil(self.n ** 0.5) + 1

        for i in range(2, upper_bound):
            if self.n % i == 0:
                other = self.n // i

                if i not in self.__prime_factors and self._is_prime(i):
                    self.__prime_factors.add(i)

                if other not in self.__prime_factors and self._is_prime(other):
                    self.__prime_factors.add(other)

        if not self.__prime_factors and self.n > 1:
            self.__prime_factors.add(self.n)

    def _is_prime(self, val):
        """Checks if *val* is a prime number or not"""
        if val in self.__primes:
            return self.__primes[val]
        elif val < 2:
            self.__primes[val] = False
            return False

        upper_bound = math.ceil(val ** 0.5) + 1

        for i in range(2, upper_bound):
            if val != i and val % i == 0:
                self.__primes[val] = False
                return False

        self.__primes[val] = True
        return True

if __name__ == "__main__":
    print("Please enter a positive integer to see its prime factors")
    print(PrimeFactorization(int(input())).get_prime_factors())
