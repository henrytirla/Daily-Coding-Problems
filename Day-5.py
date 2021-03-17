"""Given an array of integers, return a new array where each element in the new array
is the number of smaller elements to the right of that element in the original input
array.
For example, given the array [3, 4, 9, 6, 1],
return [1, 1, 2, 1, 0],
since:


• There is 1 smaller element to the right of 3
• There is 1 smaller element to the right of 4
• There are 2 smaller elements to the right of 9
• There is 1 smaller element to the right of 6
• There are no smaller elements to the right of 1"""
array = [3,4,9,6,1]


new_array =[]
for i in range(len(array)):
    count =0
    for j in range(1+i,len(array)):
        if array[j] < array[i]:
             count += 1
             new_array.append(count)
print(new_array)


"""O(n) Solution Tips

• Iterate backwards over the input list
• Maintain a sorted list seen of the elements we've seen so far
• Look at seen to see where the current element would fit in

"""


import bisect
def smaller_counts(array):
    result = []
    seen=[]
    for num in reversed(array):
        i = bisect.bisect_left(seen, num)
        result.append(i)
        bisect.insort(seen, num)
    return list(reversed(result))