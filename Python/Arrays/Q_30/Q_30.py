"""Apartment Hunting
You're looking to move into a new apartment on specific street, and you're given a list of contiguous blocks on that street where each block contains an apartment that you could move into.

You also have a list of requirements: a list of buildings that are important to you. For instance, you might value having a school and a gym near your apartment. The list of blocks that you have contains information at every block about all of the buildings that are present and absent at the block in question. For instance, for every block, you might know whether a school, a pool, an office, and a gym are present.

In order to optimize your life, you want to pick an apartment block such that you minimize the farthest distance you'd have to walk from your apartment to reach any of your required buildings.

Write a function that takes in a list of contiguous blocks on a specific street and a list of your required buildings and that returns the location (the index) of the block that's most optimal for you.

If there are multiple most optimal blocks, your function can return the index of any one of them.

Sample Input
blocks = [
  {
    "gym": false,
    "school": true,
    "store": false,
  },
  {
    "gym": true,
    "school": false,
    "store": false,
  },
  {
    "gym": true,
    "school": true,
    "store": false,
  },
  {
    "gym": false,
    "school": true,
    "store": false,
  },
  {
    "gym": false,
    "school": true,
    "store": true,
  },
]
reqs = ["gym", "school", "store"]
Sample Output
3 // at index 3, the farthest you'd have to walk to reach a gym, a school, or a store is 1 block; at any other index, you'd have to walk farther"""

blocks = [
    {
        "gym": False,
        "school": True,
        "store": False,
    },
    {
        "gym": True,
        "school": False,
        "store": False,
    },
    {
        "gym": True,
        "school": True,
        "store": False,
    },
    {
        "gym": False,
        "school": True,
        "store": False,
    },
    {
        "gym": False,
        "school": True,
        "store": True,
    },
]
reqs = ["gym", "school", "store"]

def apartmentHunting(blocks, reqs):
    n = len(blocks)
    distanceStoring = [dict() for _ in range(n)]

    # l -> r
    for i in range(n):
        for reg in reqs:
            distanceStoring[i][reg] = float('inf')

            if blocks[i][reg]:
                distanceStoring[i][reg] = 0
            elif i > 0:
                distanceStoring[i][reg] = distanceStoring[i - 1][reg] + 1


    # r -> l
    for i in range(n - 1, -1, -1):
        for reg in reqs:
            if blocks[i][reg]:
                distanceStoring[i][reg] = 0
            else:
                if i < n - 1:
                    distanceStoring[i][reg] = min(distanceStoring[i + 1][reg] + 1, distanceStoring[i][reg])

                    # compare
    res = [0, max(distanceStoring[0].values())]
    #This code block is responsible for finding the block with the maximum minimum distance to any required building.
    for i in range(1, n):
        maxValue = max(distanceStoring[i].values())

        if res[1] > maxValue:
            res[0] = i
            res[1] = maxValue

    return res[0]



if __name__ == '__main__':
    print(apartmentHunting(blocks,reqs))


"""In summary, the solution first calculates the distances from each block to the required buildings in both directions (left to right and right to left) using dynamic programming. Then, it finds the block with the maximum minimum distance to any required building and returns its index as the optimal block."""


