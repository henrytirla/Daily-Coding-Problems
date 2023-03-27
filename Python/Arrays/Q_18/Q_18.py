"""
Array Of Products
Write a function that takes in a non-empty array of integers and returns an array of the same length,
where each element in the output array is equal to the product of every other number in the input array.

In other words, the value at output[i] is equal to the product of every number in the input array other than input[i].

Note that you're expected to solve this problem without using division.

Sample Input
array = [5, 1, 4, 2]
Sample Output
[8, 40, 10, 20]
// 8 is equal to 1 x 4 x 2
// 40 is equal to 5 x 4 x 2
// 10 is equal to 5 x 1 x 2
// 20 is equal to 5 x 1 x 4


"""

arr=[5,1,4,2]

# Copyright © 2022 AlgoExpert LLC. All rights reserved.

# O(n) time | O(n) space - where n is the length of the input array
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]


    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]



    return products

print(arrayOfProducts(arr))





# def arrayOfProducts(array):
#     # create result array with size array
#     results = [0] * len(array)
#     # set first index to all values ahead, set index to 1
#     # and pass in value we don't want to calculate in index
#     # 0 forward, since indices ahead need this value
#     results[0] = array_helper(array, 1, results, array[0])
#     return results
#
#
# def array_helper(array, index, results, value):
#     # base case, if index is equal to array length then return 1
#     if index == len(array):
#         return 1
#     # val will always eqaul the multplication of all indices ahead of
#     # current index, in the recursive call increment index, and pass in
#     # value, which will be the multplication of all values before the current
#     # index, multiplied by the current index
#     val = array_helper(array, index + 1, results, array[index] * value)
#     # we set the current index to all past multiplied values * all feature
#     # multiplied values
#     results[index] = value * val
#     # then we return all feature multiplied values to the previous call
#     # this requires we multiply the current value at index * all the
#     # feature multiplied values we have received ahead of this index
#     return array[index] * val

# new_arr=[]
# product= [1 for _ in range(len(arr))]
# for i in range(len(arr)):
#     runningProduct= 1
#     for j in range(len(arr)):
#         if i!=j:
#             runningProduct *= arr[j]
#     product[i]= runningProduct
#
#
#
# print(product)

