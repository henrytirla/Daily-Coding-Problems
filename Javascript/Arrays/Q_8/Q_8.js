/**

Given an integer array nums and an integer k, return the k most frequent elements.
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


**/
let nums =[3,2,1,5,5,5,5,2]
//let nums = [1,1,1,2,2,3]
let k = 2
function MostFrequent(arr,k){
     var count = new Map();
     const bucket = new Array(arr.length + 1).fill()
         .map(() => []);


     for(num in arr){
          if (count.size !== 0 && count.has(arr[num])){
               count = count.set(arr[num],1+ count.get(arr[num]))
          }
          else{
               count = count.set(arr[num],1);}
     }
     for (const [key, value] of count.entries()) {
          bucket[value].push(key);

          //freq[value].push(key)

     }
     var res=[]
     for(let i= bucket.length-1; i>=0; i--){
          for(n in bucket[i]){
               res.push(bucket[i][n])
               if(res.length ===k){
                    return  res

               }
          }
     }






}

console.log(MostFrequent(nums,k))