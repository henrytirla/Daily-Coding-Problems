"""This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place."""


def twoNumberSum(arr, targetSum):
    # Write your code here.
   arr.sort()
   left =0
   right = len(arr)-1
   while left < right:
       currentSum = arr[left] + arr[right]

       if currentSum == targetSum:
          return [arr[left] ,arr[right]]
       elif currentSum < targetSum:
            left += 1
       elif currentSum > targetSum:
            right -= 1
   return []



arr= [3, 5, -4, 8, 11, 1, -1, 6]
sum = 10

print(twoNumberSum(arr,sum))

