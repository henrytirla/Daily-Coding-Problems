/**

Sorted Squared Array
Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order.

Sample Input
array = [1, 2, 3, 5, 6, 8, 9]
Sample Output
[1, 4, 9, 25, 36, 64, 81]

**/

function sortedSquaredArray(array){
  var sorted_arr = new Array(array.length);

  var leftIdx = 0;
  var rightIdx= array.length-1;

  for (let i = rightIdx; i>-1; i--){
    var  start = array[leftIdx]**2;
    var end = array[rightIdx] **2;

    if (end>start){
      sorted_arr[i] =end;
      rightIdx -= 1;
    }
    else{
      sorted_arr[i] = start;
      leftIdx += 1;
    }

  }

 return sorted_arr
}


var array = [1, -12, 3, -5, 6, 8, 9];


console.log(sortedSquaredArray(array))
