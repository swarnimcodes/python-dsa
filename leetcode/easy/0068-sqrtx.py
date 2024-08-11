class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        left, right = 1, x

        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


def test_mySqrt():
    solution = Solution()

    assert solution.mySqrt(4) == 2, "Test case 1 failed"
    assert solution.mySqrt(8) == 2, "Test case 2 failed"
    assert solution.mySqrt(0) == 0, "Test case 3 failed"
    assert solution.mySqrt(1) == 1, "Test case 4 failed"
    assert solution.mySqrt(9) == 3, "Test case 5 failed"
    assert solution.mySqrt(16) == 4, "Test case 6 failed"
    assert solution.mySqrt(25) == 5, "Test case 7 failed"
    assert solution.mySqrt(26) == 5, "Test case 8 failed"
    assert solution.mySqrt(2147483647) == 46340, "Test case 9 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_mySqrt()
