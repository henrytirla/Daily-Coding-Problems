"""

Write a function that takes in a non-empty array of distinct
integers and an integer representing a target sum.
The function should find all triplets in the array
that sum up to the target sum and return a two-dimensional
array of all these triplets. The numbers in each triplet should
be ordered in ascending order, and the triplets themselves should
 be ordered in ascending order with respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return
an empty array.

Sample Input
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
Sample Output
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

"""

def find_tripplets(array, targetSum):


   array.sort()
   tripplet=[]


   for i in range(len(array)):
       L = i +1
       R = len(array)-1
       while L<R:
         sum = array[i]+ array[L] + array[R]
         if sum == targetSum:
            tripplet.append([array[i], array[L] ,array[R]])
            L += 1
            R -= 1

         elif sum < targetSum:
            L +=1
         else :
            R-=1
   return tripplet

arr= [12, 3, 1, 2, -6, 5, -8, 6]

targetSum =0

print(find_tripplets(arr,targetSum))



"""O(n)3 Solution
In this case, the time complexity is O(n^3) because the number of iterations of the outermost loop
(which has a time complexity of O(n)) is multiplied by the number of iterations of the middle loop 
(which also has a time complexity of O(n)), which is in turn multiplied by the number of iterations of the innermost loop
 (also O(n)). This results in a total time complexity of O(n^3).



"""
# def find_triplets(arr, target_sum):
#     triplets = []
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             for k in range(j+1, len(arr)):
#                 if arr[i] + arr[j] + arr[k] == target_sum:
#                     triplets.append([arr[i], arr[j], arr[k]])
#     return triplets