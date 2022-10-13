
"""
Validate Subsequence
Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same
 order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an array and the array itself are both valid subsequences of the array.

Sample Input
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

"""
def checkSequenc(arr,sequence):
    arr.sort()
    sequence.sort()
    arr_pointer =0
    sequence_pointer =0
    while arr_pointer < len(arr) and sequence_pointer < len(sequence):
         if arr[arr_pointer] == sequence[sequence_pointer]:
            sequence_pointer+= 1
         arr_pointer +=1

    return sequence_pointer == len(sequence)



arr = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

print(checkSequenc(arr,sequence))





