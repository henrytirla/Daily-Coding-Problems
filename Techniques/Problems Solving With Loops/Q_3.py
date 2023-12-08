"""Given an array X of n integers, write a program to check if the array is a valid mountain array or not.

The array X is a mountain array if and only if n >= 3 and there exists some i (0 < i < n -1)
such that: X[0] < X[1] <...< X[i-1] < X[i] and X[i] > X[i+1] > ...> X[n-1].

In other words, the array is a valid mountain when it is first strictly increasing and then strictly decreasing


Examples
Input: X[] = [5, 2, 1, 4], Output: false

Input: X[] = [5, 8, 8], Output: false

Input: X[] = [1, 2, 6, 5, 3], Output: true
"""

def test_mountain_array():
    sol= Solution()

    assert sol.validMountain([1,2,6,5,3]) == True

    assert sol.validMountain([1,2]) == False

    assert sol.validMountain([5,8,8]) == False

    assert sol.validMountain([5,2,1,4])== False



class Solution:
    def validMountain(self,arr:list[int])-> bool:
        n = len(arr)
        if n < 3:
            return False
        i=0
        #Going up the mountain
        while i< n-1 and arr[i]< arr[i+1]:
            i+=1
        # Check if i is at the start or end of the array
        if i==0 or i==n-1:
           return False
        # Going Down the mountain
        while i < n-1 and arr[i] > arr[i+1]:
             i+=1

        if i== n-1:
            return True
        else:
            return False



 #Alternative Solution
# def validMountain(X, n):
#     left = 0
#     right = n - 1
#     while left < n - 1 and X[left] < X[left + 1]:
#         left = left + 1
#
#     while right > 0 and X[right - 1] > X[right]:
#         right = right - 1
#
#     if left > 0 and left == right and right < n - 1:
#         return True
#     else:
#         return False



