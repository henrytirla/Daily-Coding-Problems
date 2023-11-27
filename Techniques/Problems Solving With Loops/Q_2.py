"""Given an integer array X[] of size n, write a program to find all the leaders in the array X[].
An element is a leader if it is strictly greater than all the elements to its right side.

The last element of an array is a leader by default.
The largest element of an array is also a leader by default.
Suppose all the array elements are unique.
Ordering in the output doesn’t matter.
"""

def test_find_leaders():
    sol= Solution()
    arr = [16, 17, 4, 3, 5, 2],

    Output: [17, 5, 2]
    assert sol.find_leaders([16, 17, 4, 3, 5, 2]) ==[2,5,17]

class Solution:
    def find_leaders(self,arr:list[int])-> int:
        leaders = []
        max_so_far = -1
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > max_so_far:
                leaders.append(arr[i])
                max_so_far = arr[i]
        return leaders



if __name__ == '__main__':
    sol= Solution()
    arr=[16, 17, 4, 3, 5, 2]

    print(sol.find_leaders(arr))
