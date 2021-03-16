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

def Maxsubarray(array):   ##Solves without wrapping around
    max_end_here = 0
    max_so_far =0
    for x in array:
        max_end_here = max(x,max_end_here + x)
        max_so_far = max(max_so_far,max_end_here)

    return max_so_far
       


print(Maxsubarray([3,-2,5,-1]))