class MySort(object):
    """Class that has implementations for some sort algorithms.

    Since it is currently composed of static methods, no need for __init__
    """
    @staticmethod
    def merge_sort(to_sort):
        """Performs a merge sort on the given list. It returns a new sorted list and does it modify the given list"""

        def merge_sort_helper(left, right):
            """Helper function. Returns a sorted merge list."""
            if left >= right:
                return [to_sort[left]]

            mid = (left + right) // 2
            return merge(merge_sort_helper(left, mid), merge_sort_helper(mid + 1, right))

        def merge(list_1, list_2):
            """Merge function that merges the two given lists in sorted order and returns sorted list."""
            result, i, i_max, j, j_max = [], 0, len(list_1), 0, len(list_2)

            while i < i_max or j < j_max:
                if i == i_max:
                    result.append(list_2[j])
                    j += 1
                elif j == j_max:
                    result.append(list_1[i])
                    i += 1
                elif list_1[i] > list_2[j]:
                    result.append(list_2[j])
                    j += 1
                else:
                    result.append(list_1[i])
                    i += 1

            return result

        if len(to_sort) == 0:
            return []

        return merge_sort_helper(0, len(to_sort) - 1)

    @staticmethod
    def bubble_sort(to_sort):
        """Uses bubble sort to sort *to_sort*. Returns a new sorted array instead of doing it in-place."""
        result = list(to_sort)
        to_sort_len = len(to_sort)
        for i in range(0, to_sort_len):
            for j in range(1, to_sort_len - i):
                if result[j] < result[j-1]:
                    result[j], result[j-1] = result[j-1], result[j]

        return result

