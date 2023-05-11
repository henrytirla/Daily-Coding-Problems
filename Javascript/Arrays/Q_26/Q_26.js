/**
 Largest Range
 Write a function that takes in an array of integers and returns an array of length 2
 representing the largest range of integers contained in that array.

 The first number in the output array should be the first number in the range,
 while the second number should be the last number in the range.

 A range of numbers is defined as a set of numbers that come right after each other i
 n the set of real integers. For instance, the output array [2, 6]
 represents the range {2, 3, 4, 5, 6}, which is a range of length 5.
 Note that numbers don't need to be sorted or adjacent in the input array
 in order to form a range.

 You can assume that there will only be one largest range.

 Sample Input
 array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
 Sample Output
 [0, 7]
 */

function largestRange(array) {
    let numSet = new Set(array);
    let maxLength = 0;
    let bestRange = [];

    for (let num of array) {
        if (!numSet.has(num - 1)) {
            let currentNum = num;
            while (numSet.has(currentNum)) {
                currentNum++;
            }

            let currentLength = currentNum - num;

            if (currentLength > maxLength) {
                maxLength = currentLength;
                bestRange = [num, currentNum - 1];
            }
        }
    }

    return bestRange;
}


let array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6];
console.log(largestRange(array));
module.exports=largestRange;
