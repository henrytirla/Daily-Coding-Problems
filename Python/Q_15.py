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




Note:
Non-decreasing means that no element is less than the element before it
Non-increasing means not becoming progressively greater

Example to fully comprehend unecessary convoluted question grammar
eg  array =[1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11]

It is not monotonic.

A monotonic array is an array in which the elements either strictly increase or strictly decrease as we go through the array from left to right.
 In this array, the elements do not have a consistent increasing or decreasing pattern.

For example, the element 2 is followed by the element 3, which is higher, but then the element 4 is followed by the element 5, which is also higher.
The element 5 is followed by two more elements 5, and then the element 6 is followed by the element 7.
After the element 8, the element 7 is followed by the element 9, which is higher.

Therefore, this array is not monotonic.




"""




def isMonotonic(arr):
    # Check if the array is empty or has only one element
    if len(arr) <= 1:
        return True

    # Check if the array is non-decreasing or non-Increasing
    nonDecreasing = True
    nonIncreasing = True

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            nonDecreasing= False


        elif arr[i] > arr[i - 1]:
            nonIncreasing= False


    return nonIncreasing or nonDecreasing

#array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

array= [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11]
print(isMonotonic(array))

