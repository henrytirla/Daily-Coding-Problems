"""

Given an integer array nums, return true if any value appears at least twice in
the array return true,
and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

My algorithm
use two pointer one at the begining and one at end
add each value as key with value false
if key found hash return true
"""

def DuplicateNum(arr):
    hashset = set()
    for num in range(len(arr)):
        if arr[num] in hashset:
             return True
        hashset.add(arr[num])
    return False



arr =[1,2,3,4,5,6,3]

if __name__ == '__main__':
    print(DuplicateNum(arr))







