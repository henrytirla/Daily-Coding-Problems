"""Write a program to find the equilibrium index of an array. The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

In other words, the equilibrium index of an array is an index 'i' such that the sum of elements at indices less than 'i' is equal to the sum of elements at indices greater than 'i'. A[0] + A[1] + ... + A[i - 1] = A[i + 1] + ... + A[n - 1], where 0 <= i <= n - 1.

Problem note:

For i = 0, we assume that the sum of elements at lower indexes is equal to 0.
For i = n - 1, we assume that the sum of elements at higher indexes is equal to 0.
Example 1:
Input: A[] = [-7, 1, 5, 2, -4, 3, 0], Output: 3

Explanation: 3 is an equilibrium index, i.e., A[0] + A[1] + A[2] = A[4] + A[5] + A[6] = -1.

Example 2:
Input: A[] = [0, 1, 3, -2, -1], Output: 1

Explanation: 1 is an equilibrium index, i.e., A[0] = A[2] + A[3] + A[4] = 0.

Example 3:
Input: A[] = [1, 2, -2, -1], Output: -1

Explanation: There is no such equilibrium index in the array.
"""

def test_find_Equilibrum():
    sol= Solution()

    #Testcases
    assert sol.find_Equilibrum([0, 1, 3, -2, -1])==1
    assert sol.find_Equilibrum([1, 2, -2, -1])==-1



class Solution:
    #Non Optimal Approach O(n2) Time Complexity
    # def find_Equilibrum(self,arr:list[int])->int:
    #     n= len(arr)
    #
    #     for i in range(n):
    #         leftSide = sum(arr[:i])
    #         rightSide= sum(arr[i+1:])
    #
    #         if leftSide== rightSide:
    #             return i
    #     return -1


    def find_Equilibrum(self,arr:list[int])->int:
        n= len(arr)

        prefix_sum = [0] * n
        prefix_sum[0] = arr[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + arr[i]

        for i in range(n):
            # Calculate the sum of elements to the left using prefix sum
            left_sum = prefix_sum[i] - arr[i]

            # Calculate the sum of elements to the right using prefix sum
            right_sum = prefix_sum[-1] - prefix_sum[i]

            if left_sum == right_sum:
                return i

        return -1