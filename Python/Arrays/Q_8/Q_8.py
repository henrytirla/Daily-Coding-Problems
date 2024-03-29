"""
Given an integer array nums and an integer k,
return the k most frequent elements.
You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


#Solution Explanation
https://www.youtube.com/embed/YPTqKIgVk-k
"""
#nums = [1,1,1,2,2,3]
#nums= [3,2,1,5,5,5,5,2]
nums = [1,1,2,2,2,3]
k = 2

def MostFrequent(arr,k):
    count={}
    freq = [[]  for i in  range(len(arr)+1)]
    for n in arr:
      count[n] = 1 + count.get(n,0)
    for number,num_count in count.items():
        freq[num_count].append(number)

    res=[]
    for i in range(len(freq)-1,0,-1):
        for i in freq[i]:
            res.append(i)
            if (len(res)== k):
                return res




    return freq



if __name__ == '__main__':
    print(MostFrequent(nums, k))