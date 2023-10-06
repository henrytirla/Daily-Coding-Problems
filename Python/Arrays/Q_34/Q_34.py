"""Majority Element
Write a function that takes in a non-empty,
unordered array of positive integers and returns the array's majority element
without sorting the array and without using more than constant space.

An array's majority element is an element of the array that appears in over half of its indices.
Note that the most common element of an array (the element that appears the most times in the array)
isn't necessarily the array's majority element; for example, the arrays [3, 2, 2, 1] and [3, 4, 2, 2, 1]
 both have 2 as their most common element, yet neither of these arrays have a majority element,
 because neither 2 nor any other element appears in over half of the respective arrays' indices.

You can assume that the input array will always have a majority element."""

#Boyer-Moore Voting Algorithm. This algorithm effectively finds the majority element in a single pass through the array, maintaining a counter for the majority element candidate.

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count = 0
        ans = None
        for num in nums:
            if count == 0:
                ans = num
            if num == ans:
                count += 1
            else:
                count -= 1  # if count == 0, then ans is not the majority element
        return ans


if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()

    # Define a test list
    test_list = [3, 3, 4, 2, 4, 4, 2, 4, 4]

    # Call the majorityElement method and print the result
    print("The majority element is:", sol.majorityElement(test_list))