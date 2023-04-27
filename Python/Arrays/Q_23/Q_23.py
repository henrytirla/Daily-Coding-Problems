"""

Missing Numbers
You're given an unordered list of unique integers nums in the range [1, n],
where n represents the length of nums + 2.
This means that two numbers in this range are missing from the list.

Write a function that takes in this list and
returns a new list with the two missing numbers,
sorted numerically.

Sample Input
nums = [1, 4, 3]
Sample Output
[2, 5]  // n is 5, meaning the completed list should be [1, 2, 3, 4, 5]

"""

def missingNumbers(nums):
    # Write your code here.
    res=[]
    n= len(nums)+2

    for i in range(1,n+1):

        if i not in nums:
           res.append(i)

    return res

nums = [1, 4, 3]
print(missingNumbers(nums))


"""The time complexity of this solution is O(n), where n is the length of the input list nums.

The function iterates over a range of numbers from 1 to n+1, and checks if each number is present 
in the input list nums using the in operator. This operation takes O(n) time in the worst case, 
since it needs to search through the entire list to find the element (if it is not present).

The space complexity of this solution is also O(n), since we need to create a new list res to store the missing numbers, 
and this list can have a maximum size of n-2 (i.e., if all numbers from 1 to n are missing, except for the two in nums)."""