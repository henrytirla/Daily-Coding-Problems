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

def Maxsubarray(array):
    max_sub = 0
    for i in range(len(array)-1):
        for j in range(i,len(array)):
            max_sub= max(max_sub,sum(array[i:j]))
    return max_sub


print(Maxsubarray([3,-2,5,-1]))