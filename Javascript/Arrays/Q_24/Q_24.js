/**
 Write a function that takes in a non-empty array of distinct integers and an integer
 representing a target sum. The function should find all quadruplets in the array that
 sum up to the target sum and return a two-dimensional array of all these quadruplets
 in no particular order.

 If no four numbers sum up to the target sum, the function should return an empty array.

 Sample Input
 array = [7, 6, 4, -1, 1, 2]
 targetSum = 16
 Sample Output
 [[7, 6, 4, -1], [7, 6, 1, 2]] // the quadruplets could be ordered differently
 */

function FourNumberSums(array,targetSum){
    let PairSum={}
    let quadruplets=[]

    for(i=1;i<=array.length;i++){
        for(j=i+1;j<=array.length;j++){
            const currentSum= array[i] + array[j]
            const difference= targetSum -currentSum

            if(difference in PairSum){
                for(const pair of PairSum[difference]){
                    quadruplets.push([...pair ,array[i],array[j]])
                }
            }
        }
        for (let k = 0; k < i; k++) {
            const currentSum = array[i] + array[k];
            if (!(currentSum in PairSum)) {
                PairSum[currentSum] = [[array[k], array[i]]];
            } else {
                PairSum[currentSum].push([array[k], array[i]]);
            }
        }
    }


    return quadruplets
}


let array= [7, 6, 4, -1, 1, 2]
let targetNum= 16

console.log(FourNumberSums(array,targetNum))

module.exports= FourNumberSums;