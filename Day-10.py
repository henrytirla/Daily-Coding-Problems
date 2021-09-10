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

reference : Algoexpert.io
"""



def SortArray(arr):
    output_array = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            pass
        if arr[i] > arr[j]:
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;

                x = arr[i] ** 2
                output_array.append(x)
        else:
                x = arr[i] ** 2
                output_array.append(x)

    return output_array

print(SortArray([1,2,3,5,6,8,9]))






