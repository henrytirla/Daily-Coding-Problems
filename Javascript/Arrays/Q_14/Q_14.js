/**
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
 */


function MoveElement(arr,tomove){
    let leftIdx=0;
    let rightIdx= arr.length-1;
    while(leftIdx < rightIdx){
        if (arr[rightIdx]=== tomove){
            rightIdx-=1;
        }
        else if( arr[leftIdx]!== tomove){
               leftIdx+=1
        }
        else if (arr[leftIdx]=== tomove && arr[rightIdx]!== tomove){
                [arr[leftIdx],arr[rightIdx]]= [arr[rightIdx],arr[leftIdx]]
                rightIdx-=1
                leftIdx+=1
        }
    }
    return arr
}


/** Solution 2 **/

// function MoveElement(arr,tomove){
//     let tmp =0;
//     for(let i=0;i<arr.length;i++){
//          if(arr[i] != tomove){
//              [arr[i],arr[tmp]]= [arr[tmp],arr[i]]
//              tmp +=1
//          }
//     }
//     return arr
// }


array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

console.log(MoveElement(array,toMove))