/**
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?



**/
function ProductSum(arr){
    var prefix_array=[];
    for (let i=0; i< arr.length; i++){
        if (prefix_array.length != 0){
            prefix_array.push(prefix_array[prefix_array.length-1]* arr[i]);

        }
        else{
            prefix_array.push(arr[i]);

        }
    }
    var suffix_array =[];
    var new_arr = arr.reverse();
    for (let i=0; i< new_arr.length; i++){
        if(suffix_array.length != 0){
            suffix_array.push(suffix_array[suffix_array.length-1] * new_arr[i] )}
        else{
            suffix_array.push(new_arr[i])
        }

    }
    suffix_array = suffix_array.reverse()
    //console.log(prefix_array)
    //console.log(suffix_array)

    var result = [];

    for (let i =0; i<arr.length; i++){

        if (i == 0){

            result.push(suffix_array[i+1])

        }
        else if(i == arr.length -1){
            result.push(prefix_array[i-1])
        }
        else{
            result.push(prefix_array[i-1] * suffix_array[i+1])
        }


    }
    return result
}

var arr=[3,2,1];

console.log(ProductSum(arr))


