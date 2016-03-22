import sys
from my_sort import MySort
from random import randint


def create_randomized_list():
    upper_bound = randint(100, 500)
    return [randint(1 - sys.maxsize, sys.maxsize) for _ in range(0, upper_bound)]


# Merge sort tests
def test_merge_sort_empty_test():
    assert MySort.merge_sort([]) == []


def test_merge_sort_single_ele():
    assert MySort.merge_sort([1]) == [1]


def test_merge_sort_random_tests():
    for _ in range(0, 10):
        random_list = create_randomized_list()
        assert sorted(random_list) == MySort.merge_sort(random_list)


# Bubble sort tests
def test_bubble_sort_empty_test():
    assert MySort.bubble_sort([]) == []


def test_bubble_sort_single_ele():
    assert MySort.bubble_sort([1]) == [1]


def test_bubble_sort_random_tests():
    for _ in range(0, 10):
        random_list = create_randomized_list()
        assert sorted(random_list) == MySort.bubble_sort(random_list)

