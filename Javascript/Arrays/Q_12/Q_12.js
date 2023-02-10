/**
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should find all triplets in the array that sum up to the target sum
and return a two-dimensional array of all these triplets. The numbers in each triplet
should be ordered in ascending order, and the triplets themselves
should be ordered in ascending order with respect to the numbers they hold.

If no three numbers sum up to the target sum,
the function should return an empty array.



**/


function findTriplets(arr, targetSum) {
    // Sort the input array
    arr.sort((a, b) => a - b);

    const triplets = [];
    // Iterate over the array with two pointers: left and right
    for (let i = 0; i < arr.length; i++) {
        let left = i + 1;
        let right = arr.length - 1;
        while (left < right) {
            // Calculate the current sum
            const currentSum = arr[i] + arr[left] + arr[right];
            // If the current sum is equal to the target sum, add the triplet to the result list
            if (currentSum === targetSum) {
                triplets.push([arr[i], arr[left], arr[right]]);
                left += 1;
                right -= 1;
            }
            // If the current sum is less than the target sum, move the left pointer to the right to increase the sum
            else if (currentSum < targetSum) {
                left += 1;
            }
            // If the current sum is greater than the target sum, move the right pointer to the left to decrease the sum
            else {
                right -= 1;
            }
        }
    }
    return triplets;
}

let arr= [12, 3, 1, 2, -6, 5, -8, 6]

let targetSum =0

console.log(findTriplets(arr,targetSum))