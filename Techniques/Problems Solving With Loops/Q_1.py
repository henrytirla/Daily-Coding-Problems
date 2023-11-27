"""Given an input array height[] representing the heights of buildings, write a program to count the number of buildings facing the sunset. It is assumed that the heights of all buildings are distinct.

Examples
Input: height[] = [7, 4, 8, 2, 9], Output: 3 Explanation: As 7 is the first element, it can see the sunset. Similarly, 8 and 9 can see the sunset. 4 and 2 can't see the sunset because 7 and 8 are hiding it.

Input: height[] = [2, 3, 4, 5], Output: 4

"""


class Solution():

    def count_Building(self, buildings: list[int]) -> int:
        currentMax= buildings[0]
        buildingCount= 1
        for i in range(0,len(buildings)):
            if  buildings[i] > currentMax:
                currentMax = buildings[i]
                buildingCount+=1

        return buildingCount



if __name__ == "__main__":
    sol = Solution()

    building_list = [7, 4, 8, 2, 9]

    # Call the count_Building method and print the result
    print("The Number of Buildings Facing the sun:", sol.count_Building(building_list))


def test_countBuilding():
    sol = Solution()

    # Testcase1
    assert sol.count_Building([7, 4, 8, 2, 9]) == 3
    # Testcase2
    assert sol.count_Building([2, 3, 4, 5]) == 4


""""Critical ideas to think!
How can we modify the above code to also return the building that can see the sunset?
How can we modify the above code when some buildings have the same height? Assume that a building of the same height will block the one after it.
Is it possible to solve this problem using a stack?"""