/**
 Subarray Sort
 Write a function that takes in an array of at least two integers and that returns an array
 of the starting and ending indices of the smallest subarray in the input array that needs
 to be sorted in place in order for the entire input array to be sorted (in ascending order).

 If the input array is already sorted, the function should return [-1, -1].

 Sample Input
 array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
 Sample Output
 [3, 9]
 */

function subarraySort(array) {
    let leftValue = -1;
    let rightValue = -1;
    let maxValue = array[0];

    for (let i = 1; i < array.length; i++) {
        if (array[i] < maxValue) {
            leftValue = i;
        } else {
            maxValue = array[i];
        }
    }

    let minValue = array[array.length - 1];

    for (let i = array.length - 1; i >= 0; i--) {
        if (array[i] > minValue) {
            rightValue = i;
        } else {
            minValue = array[i];
        }
    }

    return [rightValue, leftValue];
}

const array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19];
console.log(subarraySort(array));

module.exports=subarraySort;
