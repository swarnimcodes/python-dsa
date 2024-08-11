"""_summary_
QUESTION: Alice has some cards with numbers written on them.
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
Write a function to help Bob locate the card.
"""

import unittest


def bs(sorted_card_list: list[int], desired_num: int) -> int:
    left_ptr: int = 0
    right_ptr: int = len(sorted_card_list) - 1
    while left_ptr <= right_ptr:
        mid: int = left_ptr + (right_ptr - left_ptr) // 2

        if (
            sorted_card_list[mid] == desired_num
            and sorted_card_list[mid - 1] != desired_num
        ):
            return mid
        elif sorted_card_list[mid] < desired_num:
            left_ptr = mid + 1
        else:
            right_ptr = mid - 1
    return -1


class TestBinarySearch(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(bs([], 42), -1)

    def test_element_not_in_list(self):
        sorted_list = [10, 20, 30, 40, 50]
        self.assertEqual(bs(sorted_list, 35), -1)

    def test_element_at_beginning(self):
        sorted_list = [10, 20, 30, 40, 50]
        self.assertEqual(bs(sorted_list, 10), 0)

    def test_element_at_end(self):
        sorted_list = [10, 20, 30, 40, 50]
        self.assertEqual(bs(sorted_list, 50), 4)

    def test_element_in_middle(self):
        sorted_list = [10, 20, 30, 40, 50]
        self.assertEqual(bs(sorted_list, 30), 2)

    def test_duplicate_elements(self):
        sorted_list = [10, 20, 20, 20, 30, 30, 30, 30, 30, 30, 30, 40, 50]
        self.assertEqual(bs(sorted_list, 30), 4)


if __name__ == "__main__":
    unittest.main()
