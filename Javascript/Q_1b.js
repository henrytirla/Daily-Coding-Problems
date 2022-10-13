/**

This problem was recently asked by Google.

Given a list of numbers and a number k,
return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17,
return true since 10 + 7 is 17.

Note-toself: As in the python section i will use a Binary tree to solve this problem


**/

//import "d3-array";

var arr= [10, 15, 3, 7];
var k = 17;
function Check4Sum(arr,k,){
  arr.sort();
  let num = {};
  	for (let i of arr){
  		  if(k -i in num){
  				 return true;
  			}else{
  				num[i]= false;
  			}
  	}
  return false;



}

console.log(Check4Sum(arr,k))
