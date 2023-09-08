"""_summary_
Question: Two Sum
Given an array A[] of n numbers and another number x,
the task is to check whether or not there exist two elements in A[]
whose sum is exactly x.

Example: {0, -1, 2, -3, 1}, x= -2
Output: Yes
Sice -3 + 1 = -2
"""

import unittest

"""_summary_
This is the brute force approach.
Just traverse the given array/list twice
"""
def two_sum_exists_naive(given_list: list[int], two_sum: int) -> bool:
    for i in given_list:
        for j in given_list:
            if i + j == two_sum and i != j:
                return True
    return False

"""_summary_
This is similar to the brute force approach
This uses a bit more logic but still the time complexity is O(n^2)
This is because the statement if sum_difference in given list just traverses
the list and will have time complexity of O(n) in worst case
"""

def two_sum_exists_naive_2(given_list: list[int], two_sum: int) -> bool:
    for i in given_list:
        sum_difference: int = two_sum - i
        if sum_difference in given_list and sum_difference != i:
            return True
    return False

"""
Two Pointer Approach
This method is better since its time complexity is O(n) for the while loop
because in the worst case we will have to traverse the list once.

the sorted(list) method has a time complexity of O(n log(n)) and is implemented
by python using some hybrid between quicksort and mergesort to the best of my knowledge.

This approach is significantly better than the above two methods in terms of
time complexity.

If a lesser amount of memory is needed we could sort the given list in place
using the sort(list) function provided by python. This method will have similar
time complexity but will use lesser amount of space. The downside is that the
original list will not be preserved.

Left Index must always be lesser than the right index since if they are equal
we are looking at the same element and we don't want that in this case.

To delve deeper, we could implement the sorting algorithm ourselves
using quicksort technique.
"""

def two_sum_exists_two_pointer_approach(given_list: list[int], two_sum: int) -> bool:
    sorted_given_list: list[int] = sorted(given_list)
    left_index: int = 0
    right_index: int = len(sorted_given_list) -1
    while left_index < right_index:
        if sorted_given_list[left_index] + sorted_given_list[right_index] > two_sum:
            right_index = right_index - 1
        elif sorted_given_list[left_index] + sorted_given_list[right_index] < two_sum:
            left_index = left_index + 1
        elif sorted_given_list[left_index] + sorted_given_list[right_index] == two_sum:
            return True
    return False

"""
Trying to implement the two pointer approach while also implementing quicksort.

Quicksort is slightly faster than mergesort and heapsort, especially
on large and random.

It is a divid-and-conquer algorithm.

Mathematical analysis of quicksort shows that, on average, the algorithm
takes O(n log n) comparisons to sort n items.
In the worst case, it makes O(n^2) comparisons.

The recursive nature of quicksort lends itself to parellelism.

To learn more about quicksort: https://en.wikipedia.org/wiki/Quicksort
"""
def partition(arr: list[int], lo: int, hi: int) -> int:
    pivot: int = arr[hi]
    i: int = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1

def quicksort(arr: list[int], lo: int, hi: int) -> None:
    if lo < hi:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p - 1)
        quicksort(arr, p + 1, hi)

def two_sum_exists(given_list: list[int], two_sum: int) -> bool:
    n = len(given_list)
    sorted_given_list: list[int] = given_list.copy()
    quicksort(sorted_given_list, 0, n - 1)
    left_index: int = 0
    right_index: int = n - 1
    while left_index < right_index:
        current_sum: int = sorted_given_list[left_index] + sorted_given_list[right_index]
        if current_sum > two_sum:
            right_index = right_index - 1
        elif current_sum < two_sum:
            left_index = left_index + 1
        elif current_sum == two_sum:
            return True
    return False

class TestTwoSumExists(unittest.TestCase):

    def test_sum_doesnt_exist(self):
        # Test case 1: No valid two sum exists
        given_list = [1, -2, 1, 0, 5]
        two_sum = 0
        self.assertEqual(two_sum_exists(given_list, two_sum), False)

        # Test case 2: No valid two sum exists with empty list
        given_list = []
        two_sum = 5
        self.assertEqual(two_sum_exists(given_list, two_sum), False)

        # Test case 3: No valid two sum with a single element list
        given_list = [7]
        two_sum = 7
        self.assertEqual(two_sum_exists(given_list, two_sum), False)

    def test_sum_does_exist(self):
        # Test case 1: Valid two sum exists
        given_list = [1, -2, 1, 0, 5, 7, -6, 4]
        two_sum = -2
        self.assertEqual(two_sum_exists(given_list, two_sum), True)

        # Test case 2: Valid two sum exists with duplicate elements
        given_list = [1, 2, 2, 3, 4]
        two_sum = 4
        self.assertEqual(two_sum_exists(given_list, two_sum), True)

        # Test case 3: Valid two sum exists with zero
        given_list = [0, 0, 0, 0]
        two_sum = 0
        self.assertEqual(two_sum_exists(given_list, two_sum), True)

if __name__ == '__main__':
    unittest.main()