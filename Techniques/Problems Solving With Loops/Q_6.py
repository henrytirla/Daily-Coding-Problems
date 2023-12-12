"""Given an array X[] of n integers where n > 1, write a program to return an array product[] such that product[i] is equal to the product of all the elements
of X except X[i].

It's guaranteed that the product of the elements of any prefix or suffix of the array (including the entire array) fits into a 32-bit integer.
We need to solve this problem without using division operations.

"""


def test_productExceptSelf():
    assert Solution().productExceptSelf([2, 1, 3, 4]) == [12, 24, 8, 6]
    assert Solution().productExceptSelf([5, 1, 4, 2]) == [8, 40, 10, 20]
    assert Solution().productExceptSelf([1, 8, 6, 2, 4]) == [384, 48, 64, 192, 96]


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            # product of all elements to the left of nums[i], excluding nums[i] itself.
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            # product of all elements to the right of nums[i], excluding nums[i] itself.
            right[i] = right[i + 1] * nums[i + 1]
        for i in range(n):
            nums[i] = left[i] * right[i]
        return nums
