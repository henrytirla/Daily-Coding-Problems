"""
Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum. If any two numnbers in the input array sum up to the target summ
the function should return them in an array, in any order. If no two numbers sum up to the
target sum, the function should return an empty array


"""

"""
Solution Using Pointers
def twoNumberSum(arr, targetSum):

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

"""
import pytest

arr= [ 3,5,-4,8,11,1,-1,6]
targetSum =10




def twoNumberSum(arr,targetSum):
   hash_table={}
   for num in range(len(arr)):
       X= arr[num]
       Y= targetSum - X
       if Y not in hash_table:
           hash_table.update({X:'True'})



       else:
           return X,Y
   return []




if __name__ == '__main__':
    print(twoNumberSum(arr, targetSum))





