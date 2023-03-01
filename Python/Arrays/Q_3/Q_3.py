"""
Sorted Squared Array
Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order.

Sample Input
array = [1, 2, 3, 5, 6, 8, 9]
Sample Output
[1, 4, 9, 25, 36, 64, 81]

"""



def sortedSquaredArray(array):
    # Write your code here
   sorted_arr=[0 for _ in array]
   leftIdx =0
   rightIdx = len(array)-1


   for  idx in reversed(range(len(array))):
        smallValue = array[idx]
        largeValue = array[rightIdx]
        if abs(smallValue) > abs(largeValue):
           sorted_arr[idx] = smallValue ** 2
           leftIdx +=1
        else:
            sorted_arr[idx] = largeValue**2
            rightIdx-=1
   return sorted_arr







array = [-1, -2, -14, 5, 6, 8, 9]

if __name__== '__main__':
    print(sortedSquaredArray(array))







#BRUTE FORCE
# def sortedSquaredArray(array):
#         # Write your code here
#         sorted_arr = []
#         array.sort()
#
#         for num in array:
#                 sorted_arr.append(num ** 2)
#
#         return sorted_arr
#
#
# array = [1, 2, 3, 5, 6, 8, 9]
# print(sortedSquaredArray(array))