"""
Writea function that takes in a non-empty array of distinct integers and an
integer representing a target sum. If any two numnbers in the input array sum up to the target summ
the function should return them in an array, in any order. If no two numbers sum up to the
target sum, the function should return an empty array


"""

arr= [ 3,5,-4,8,11,1,-1,6]
targetSum =10




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


print(twoNumberSum(arr,targetSum))