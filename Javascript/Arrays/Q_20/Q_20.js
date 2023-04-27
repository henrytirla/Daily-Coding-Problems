/**
 Merge Overlapping Intervals
 Write a function that takes in a non-empty array of arbitrary intervals, merges any overlapping intervals, and returns the new intervals in no particular order.

 Each interval interval is an array of two integers, with interval[0] as the start of the interval and interval[1] as the end of the interval.

 Note that back-to-back intervals aren't considered to be overlapping. For example, [1, 5] and [6, 7] aren't overlapping; however, [1, 6] and [6, 7] are indeed overlapping.

 Also note that the start of any particular interval will always be less than or equal to the end of that interval.

 Sample Input
 intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
 Sample Output
 [[1, 2], [3, 8], [9, 10]]
 // Merge the intervals [3, 5], [4, 7], and [6, 8].
 // The intervals could be ordered differently.
 */

let intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]

function mergeOverlappingIntervals(intervals){
    intervals.sort()
    const resultArr = [intervals[0]];

    for (let i = 1; i < intervals.length; i++) {
        if (resultArr[resultArr.length - 1][1] >= intervals[i][0]) {
            resultArr[resultArr.length - 1][1] = Math.max(resultArr[resultArr.length - 1][1], intervals[i][1]);
        } else {
            resultArr.push(intervals[i]);
        }
    }
    return resultArr;

}

console.log(mergeOverlappingIntervals(intervals))

module.exports = mergeOverlappingIntervals;

/**The time complexity of this function is O(n * log(n)) and space complexity is O(n).
Time Complexity: The sorting step has a time complexity of O(n * log(n)),
 where n is the number of intervals.
The iteration step has a time complexity of O(n) as it iterates through all the intervals.
As the sorting step dominates the overall time complexity, the function's time complexity is O(n * log(n)).

Space Complexity: The additional space used by the function is mainly due to the resultArr array.
In the worst case, none of the intervals overlap, and resultArr has the same number of intervals as the input array.
Therefore, the space complexity of the function is O(n), where n is the number of intervals in the input array.
**/