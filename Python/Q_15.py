"""Write a function that takes in an array of integers and returns a boolean
representing whether the array is monotonic.

An array is said to be monotonic if its elements,
from left to right, are entirely non-increasing or entirely non-decreasing.

Non-increasing elements aren't necessarily exclusively decreasing;
they simply don't increase. Similarly, non-decreasing elements aren't
necessarily exclusively increasing; they simply don't decrease.

Note that empty arrays and arrays of one element are monotonic.

Sample Input
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

Sample Output
true


Algorith

Put a pointer on last array
and on start

while R<L:
 compare both pointer if L > R
 return False



"""




def isMonotonic(arr):
    # Check if the array is empty or has only one element
    if len(arr) <= 1:
        return True

    # Check if the array is non-decreasing
    nonDecreasing = True
    nonIncreasing = True

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            nonDecreasing= False


        elif arr[i] > arr[i - 1]:
            nonIncreasing= False


    return nonIncreasing or nonDecreasing

array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print(isMonotonic(array))

