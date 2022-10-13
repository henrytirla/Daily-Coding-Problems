/**
Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear
 in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a
 single number in an array and the array  itself are both valid subsequences of the array.

CREDITS https://www.algoexpert.io/
ALGO DAILY
ENJOY ALGORITHMS
**/


function checkSequence(array,sequence){

var arrIdx = 0;
var seqIdx =0;

while (arrIdx < array.length && seqIdx < sequence.length)
{

       if (array[arrIdx] == sequence[seqIdx])
       {
          seqIdx +=1;

       }
       arrIdx+=1
}
return seqIdx == sequence.length;

}

var array = [5, 1, 22, 25, 6, -1, 8, 10];
var sequence = [1, 6, -1, 10];



console.log(checkSequence(array,sequence));


