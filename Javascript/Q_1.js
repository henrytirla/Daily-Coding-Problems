/**
Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum. If any two numnbers in the input array sum up to the target summ
the function should return them in an array, in any order. If no two numbers sum up to the
target sum, the function should return an empty array




***/

function twoNumberSum(array, targetSum) {

   let l = 0;
   let r = array.length -1;

   array.sort( (a,b) => a-b );

   while(l<r) {
     let sum = array[l] + array[r];

     if( sum == targetSum )
       return [ array[l], array[r] ];
     if( sum < targetSum)
       l++;
     else
       r--;

   }
   return [];

