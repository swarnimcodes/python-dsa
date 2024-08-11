"""
Question:
Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.

Resources:
- Leetcode: https://leetcode.com/problems/contains-duplicate/
"""

import timeit
import sys

sys.setrecursionlimit(10000000)

"""
Brute Force:
"""


def cont_dupl_brute(nums: int) -> bool:
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums) - 1):
            if nums[i] == nums[j] and i != j:
                return True
    return False


"""
Sorting Approach:
Haven't checked for other approaches online.
If we sort the array using a decent algorithm (either built-in or implemented)
then we can just traverse the loop once and check if the surrounding elements
are equal.


On benchmarking, the brute force method performs better even for large arrays.
This is perhaps because of our quicksort implementation that maybe is not as
efficient as we expect.
If we change to using builtin sorted() function of python library we
see that it is significantly faster than the brute force method. So in theory
our quicksort is a better method of finding duplicates
"""


def partition(nums: list[int], lo, hi) -> int:
    pivot: int = nums[hi]
    i: int = lo - 1

    for j in range(lo, hi):
        if nums[j] <= pivot:
            i = i + 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[hi] = nums[hi], nums[i + 1]
    return i + 1


def quicksort(nums: list[int], lo, hi) -> None:
    if lo < hi:
        p = partition(nums, lo, hi)
        quicksort(nums, lo, p - 1)
        quicksort(nums, p + 1, hi)


def cont_dupl_qs(nums: int) -> bool:
    quicksort(nums, 0, len(nums) - 1)
    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i + 1] and i + 1 < len(nums):
            return True
    return False


"""
Next Approach: Hash Set
Hash Sets can only contain unique values.
They are extremely efficient.
Insertion: O(n)
Searching: O(n)
Deletion: O(n)

Time Complexity: O(n)
"""


def cont_dupl(nums: list[int]) -> bool:
    num_set: list[int] = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False


# def cont_dupl(nums: list[int]) -> bool:
#     num_set = set(nums)
#     if len(nums) > len(num_set):
#         return True
#     else:
#         return False


def main() -> None:
    nums: list[int] = [2, 1, 1, 1, 1, 12, 13, 5, 7, 9, 11, 109, -2, -4]
    time_taken = timeit.timeit(lambda: cont_dupl(nums), number=100)
    print(f"Condition: {cont_dupl(nums)}")
    print(f"TimeIt Stats: {time_taken}")


if __name__ == "__main__":
    main()
