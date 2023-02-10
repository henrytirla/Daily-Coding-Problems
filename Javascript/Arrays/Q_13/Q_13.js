/**
 Write a function that takes in two non-empty arrays of integers,
 finds the pair of numbers (one from each array) whose absolute difference is closest
 to zero, and returns an array containing these two numbers, with the number from the first
 array in the first position.

 Note that the absolute difference of two integers is the distance between them on the real number line.
 For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.

 You can assume that there will only be one pair of numbers with the smallest difference.

 Sample Input
 arrayOne = [-1, 5, 10, 20, 28, 3]
 arrayTwo = [26, 134, 135, 15, 17]
 Sample Output
 [28, 26]

 */

function find_closest_pair(arr1,arr2){
    arr1.sort((a,b) =>a-b);
    arr2.sort((a,b)=>a-b);
    let min_diff= Infinity;
    let i=0;
    let j=0;
    let closest_pair=[];

    while( i < arr1.length && j < arr2.length) {
        let diff = Math.abs(arr1[i] - arr2[j])

        if (diff < min_diff){
            min_diff = diff
            closest_pair= [[arr1[i],arr2[j]]]

        }

        if (arr1[i] < arr2[j]){
            i += 1
        }
        else{
            j+=1
        }




    }

    return closest_pair


}

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

console.log(find_closest_pair(arrayOne,arrayTwo))
