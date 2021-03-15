# Get product of all other elements
#Given an array of integers, return a new array such that each element at index i of
# the new array is the product of all the numbers in the original array except the one
# at i.
# For example, if our input was [ 1, 2, 3, 4, 5], the expected output would be [ 120,
# 60, 40, 30, 24]. If our input was [3, 2, 1],theexpectedcoutput would be [2,
# 3, 6].
# Follow-up: What if you can't use division?

# from functools import reduce
# def products(nums):
#     return [ reduce(lambda x,y: x * y, nums[:i] + nums[i+1:]) for i in range(len(nums)) ]
# print(products([3,2,1]))
# print(products([1, 2, 3, 4, 5]))


def findProduct(A):
    n = len(A)

    # use two auxiliary lists
    left = [None] * n
    right = [None] * n

    # `left[i]` stores the product of all elements in sublist `A[0…i-1]`
    left[0] = 1
    for i in range(1, n):
        left[i] = A[i - 1] * left[i - 1]

    # `right[i]` stores the product of all elements in sublist `A[i+1…n-1]`
    right[n - 1] = 1
    for j in reversed(range(n - 1)):
        right[j] = A[j + 1] * right[j + 1]

    # replace each element with the product of its left and right sublist
    for i in range(n):
        A[i] = left[i] * right[i]


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    findProduct(A)

    # print the modified list
    print(A)

