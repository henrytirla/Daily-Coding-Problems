"""

Move Element To End
You're given an array of integers and an integer.
 Write a function that moves all instances of that integer in the array to the
 end of the array and returns the array.

The function should perform this in place
 (i.e., it should mutate the input array) and doesn't need to maintain the order of the other integers.

Sample Input
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
Sample Output
[1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently

"""





#
# def Move_element(arr,tomove):
#
#     leftIdx=0
#     rightIdx=len(arr)-1
#     while leftIdx < rightIdx:
#         if arr[rightIdx] == tomove:
#            rightIdx-=1
#         elif arr[leftIdx] != tomove:
#              leftIdx +=1
#         elif arr[leftIdx] == tomove and arr[rightIdx]!= tomove:
#              arr[leftIdx], arr[rightIdx]= arr[rightIdx],arr[leftIdx]
#              rightIdx-=1
#              leftIdx +=1
#
#     return arr



"""Solution Two -- 1 3 4 in order"""
def Move_element(arr,tomove):
    tmp=0
    for i in range(len(array)):
        if array[i] != tomove:
            array[i], array[tmp] = array[tmp],array[i]
            tmp+=1
    return  array



array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2




if __name__ == '__main__':
    print(Move_element(array, toMove))


"""The time complexity of this  solution is O(n), where n is the length of the input array.
 This is because the algorithm only needs to iterate over the array once, with two pointers, 
 to move all instances of the specified integer to the end of the array.

The two pointers move toward the middle of the array until they meet,
 so the algorithm only needs to perform a constant number of operations per element in the array. 
 This means that the algorithm's time complexity is linear, or O(n), in the size of the input array"""