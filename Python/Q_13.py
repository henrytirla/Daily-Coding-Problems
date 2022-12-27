"""

Write a function that takes in two non-empty arrays of integers,
finds the pair of numbers (one from each array) whose absolute difference is closest
to zero, and returns an array containing these two numbers, with the number from the first
array in the first position.

Note that the absolute difference of two integers is the distance between them on the real number line.
For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.

You can assume that there will only be one pair of numbers with the smallest difference.

Sample Input
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
Sample Output
[28, 26]




"""

def find_closest_pair(arr1,arr2):
    arr1.sort()
    arr2.sort()

    min_diff = float('inf')
    closest_pair=[]

    i=0
    j=0

    while  i < len(arr1) and  j < len(arr2):

          diff = abs(arr1[i] -arr2[j])

          if diff < min_diff:
               min_diff = diff
               closest_pair=[arr1[i],arr2[j]]

          if arr1[i] < arr2[j]:
              i += 1

          else:
              j += 1

    return closest_pair


arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

print(find_closest_pair(arrayOne,arrayTwo))


"""
This algorithm first sorts both input arrays, and then uses two pointers (i and j) to iterate over 
the arrays simultaneously. It calculates the absolute difference between the elements at the pointers 
and updates the minimum difference and the closest pair as needed. It also moves the pointers in the 
appropriate direction (either to the right or to the left) to continue comparing the elements.

The time complexity of this algorithm is O(n log n), because the time complexity of the sorting algorithm (O(n log n)) 
is dominant over the time complexity of the two-pointer approach (O(n)).


"""

