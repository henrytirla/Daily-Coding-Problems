""""This problem was recently asked by Google.

Given a list of numbers and a number k,
return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17,
return true since 10 + 7 is 17."""






"""'''
Important to NOTE

bisect_left finds and returns the index where an element can be inserted 
and still maintain sorted order of the list



ALgorithm

1. sort list
2. T = targetsum - lst[i] ie i for all elements in lst  --  
3. Find index where current value of T can be inserted in sorted lst using bisect_left

4.  lst[index] == T 

5, Check J elif statement in case when index == i

 To understand more Binary trees I suggest the link below

https://algodaily.com/lessons/an-intro-to-binary-trees-and-search-trees
 
 
'''"""


from bisect import bisect_left
def two_sum(lst, K):
    lst.sort()

    for i in range(len(lst)):
        target = K - lst[i]
        j = binary_search(lst, target)

        # Check that binary search found the target and that it's not in the same index
        # as i. If it is in the same index, we can check lst[i + 1] and lst[i - 1] to see
        #  if there's another number that's the same value as lst[i].
        if j == -1:
            continue
        elif j != i:
            return [True ,lst[i],lst[j]]  ##

        elif j + 1 < len(lst) and lst[j + 1] == target:
            return [True ,lst[i],lst[j+1]]
        elif j - 1 >= 0 and lst[j - 1] == target:
            return [True ,lst[i],lst[j-1]]
    return False

def binary_search(lst, target):

    ind = bisect_left(lst, target)

    if  lst[ind] == target:
        return ind
    return -1

lst =[10,15,3,7]
k = 10
print(two_sum(lst,k))

# class Treenode():
#     def __init__(self):
#         self.left =None
#         self.right = None
#         self.data = None
#
#
#
#
# root= Treenode()
# root.data = "Left"
# root.left =Treenode()
# root.left.data = "Left Root data"
# root.right = Treenode()
# root.right.data = "Right Root Data"

















#
# def Suminlist(array, k):
#     sums = []
#     for i in range(len(array) - 1):
#         first_num = array[i]
#         for j in range(i + 1, len(array)):
#             second_num = array[j]
#             if first_num + second_num == k:
#                 sums.extend((first_num, second_num))
#     return sums, True
#
#
# a = Suminlist([3, 2, 1, 6], 9)
# print(a)
#Another solution

# def twoNumberSum(arr,targetSum):
#    hash_table={}
#    for num in range(len(arr)):
#        X= arr[num]
#        Y= targetSum - X
#        if Y not in hash_table:
#            hash_table.update({X:'True'})
#
#
#
#        else:
#            return X,Y
#    return []





