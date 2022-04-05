""""
Sorted Squared Array

Write a function that takes a non-empty array of integers
that are sorted in ascending order and returns a new array of
the same length with the squares of the original integers
also sorted in ascending order

sample input
array =[1,2,3,5,6,8,9]
array = [3,2,1]

sample output
[1,4,9,25,36, 64,81]
[1,4,9]
test case

try solving for [-4,1,2]
reference : Algoexpert.io
"""


def sortedSquaredArray(arr):
    # Write your code here.
    output_array = []


    for i in range(len(arr)):
        x = arr[i] ** 2
        output_array.append(x)
        output_array.sort()


    return output_array


print(sortedSquaredArray([-4,1,2]))




