"""
Zero Sum Subarray
You're given a list of integers nums.
Write a function that returns a boolean representing
whether there exists a zero-sum subarray of nums.

A zero-sum subarray is any subarray where all of the values add up to zero.
A subarray is any contiguous section of the array. For the purposes of this problem,
a subarray can be as small as one element and as long as the original array.

Sample Input
nums = [-5, -5, 2, 3, -2]
Sample Output
True // The subarray [-5, 2, 3] has a sum of 0
"""

def ZeroSubArray(array):
    sum_set={0}
    current_sum= 0
    for num in array:
        current_sum+=num

        if current_sum in sum_set:
           return True
        sum_set.add(current_sum)

    return False

if __name__ == '__main__':
    nums = [-2, -3, -1, 2, 3, 4, -5, -3, 1, 2]
    print(ZeroSubArray(nums))

