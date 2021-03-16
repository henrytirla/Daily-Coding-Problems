"""Given an array of numbers, :find the maximum sum of any contiguous subarray of
the array. For example, given the array [34, -50, 42, 14, -5, 86], the maximum
sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array
[ -5, -1, -8, -9], the maximum sum would be 0, since we would choose not to
take any elements.
Do this in O ( n) time.
Follow-up: What if the elements can wrap around? For example, given [ 8, -1, 3,
4], return 15, as we choose the numbers 3, 4, and 8 where the 8 is obtained from
wrapping around.
eg 3,-2,5,-1
"""

def maximum_circular_subarray(arr):
        max_subarray_sum_wraparound = sum(arr) - min_subarray_sum(arr)
        return max(max_subarray_sum(arr), max_subarray_sum_wraparound)

def max_subarray_sum(arr): #Solves without the wrap around Kadanes Algorithm
    max_ending_here= 0
    max_so_far =0
    for x in arr:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
       
def min_subarray_sum(arr):
    min_ending_here =0
    min_so_far = 0
    for x in arr:
        min_ending_here = min(x, min_ending_here + x)
        min_so_far = min(min_so_far, min_ending_here)
    return min_so_far

print(maximum_circular_subarray([8, -1, 3,
4]))