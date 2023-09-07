"""_summary_
QUESTION 1: Alice has some cards with numbers written on them.
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
Write a function to help Bob locate the card.
"""

def bs(sorted_card_list: list[int], desired_num: int) -> int:
    left: int = 0
    right: int = len(sorted_card_list) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if sorted_card_list[mid] == desired_num:
            return mid
        elif sorted_card_list[mid] < desired_num:
            left = mid + 1
        else:
            right = mid - 1
    return -1


import unittest

class TestBinarySearch(unittest.TestCase):

    def test_empty_list(self):
        # Test when the input list is empty
        self.assertEqual(bs([], 42), -1)

    def test_element_not_in_list(self):
        # Test when the desired number is not in the list
        sorted_list = [10, 20, 30, 40, 50]
        self.assertEqual(bs(sorted_list, 35), -1)

    def test_element_at_beginning(self):
        # Test when the desired number is at the beginning of the list
        sorted_list = [10, 20, 30, 40, 50]
        self.assertEqual(bs(sorted_list, 10), 0)

    def test_element_at_end(self):
        # Test when the desired number is at the end of the list
        sorted_list = [10, 20, 30, 40, 50]
        self.assertEqual(bs(sorted_list, 50), 4)

    def test_element_in_middle(self):
        # Test when the desired number is in the middle of the list
        sorted_list = [10, 20, 30, 40, 50]
        self.assertEqual(bs(sorted_list, 30), 2)

    def test_duplicate_elements(self):
        # Test when there are duplicate elements in the list
        sorted_list = [10, 20, 30, 30, 40, 50]
        self.assertEqual(bs(sorted_list, 30), 2)

if __name__ == '__main__':
    unittest.main()
