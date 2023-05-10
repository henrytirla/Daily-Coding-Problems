
"""
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
"""

def four_number_sum(array, target_sum):
    pair_sums = {}
    quadruplets = []

    for i in range(1, len(array)):
        for j in range(i + 1, len(array)):
            current_sum = array[i] + array[j]
            difference = target_sum - current_sum

            if difference in pair_sums:
                for pair in pair_sums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])

        for k in range(0, i):
            current_sum = array[i] + array[k]
            if current_sum not in pair_sums:
                pair_sums[current_sum] = [[array[k], array[i]]]
            else:
                pair_sums[current_sum].append([array[k], array[i]])

    return quadruplets




if __name__ == '__main__':
    arr= [7, 6, 4, -1, 1, 2]
    print(four_number_sum(arr,16))
    #print(fourNumberSum(arr,16))

