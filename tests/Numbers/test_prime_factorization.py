import pytest
from prime_factorization import PrimeFactorization


# Prime factors were received from: http://www.calculatorsoup.com/calculators/math/prime-factors.php for testing
def test_not_int():
    with pytest.raises(TypeError):
        PrimeFactorization(1.2)
    with pytest.raises(TypeError):
        PrimeFactorization([1])
    with pytest.raises(TypeError):
        PrimeFactorization({})
    with pytest.raises(TypeError):
        PrimeFactorization(None)
    with pytest.raises(TypeError):
        PrimeFactorization("1")


def test_less_than_0():
    with pytest.raises(ValueError):
        PrimeFactorization(-1)


def test_0():
    prime_test = PrimeFactorization(0)
    assert prime_test.get_prime_factors() == set()


def test_1():
    prime_test = PrimeFactorization(1)
    assert prime_test.get_prime_factors() == set()


def test_2():
    prime_test = PrimeFactorization(2)
    assert prime_test.get_prime_factors() == set([2])


def test_10():
    prime_test = PrimeFactorization(10)
    assert prime_test.get_prime_factors() == set([2, 5])


def test_31235():
    prime_test = PrimeFactorization(31235)
    assert prime_test.get_prime_factors() == set([5, 6247])


def test_997():
    prime_test = PrimeFactorization(997)
    assert prime_test.get_prime_factors() == set([997])
