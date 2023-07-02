"""This problem was asked by Mailchimp.

You are given an array representing the heights of neighboring buildings on a city street,
 from east to west.
 The city assessor would like you to write an algorithm that returns how many of these buildings
 have a view of the setting sun,
 in order to properly value the street.

For example, given the array [3, 7, 8, 3, 6, 1], you should return 3,
 since the top floors of the buildings with heights 8, 6, and 1 all have an unobstructed view to the west.

Can you do this using just one forward pass through the array?


"""
import pytest

arr=[3, 7, 8, 3, 6, 1]
def ViewSun(arr):


    count=1
    idx= len(arr)-2
    for i in reversed(range(len(arr))):
        if arr[idx] > arr[i]:
           count+=1

        idx-=1
    return count



@pytest.mark.parametrize("arr, expected_count", [
    #Testcase
    ([3, 7, 8, 3, 6, 1], 3),


])
def test_ViewSun(arr, expected_count):
    assert ViewSun(arr) == expected_count

# Run the tests
pytest.main()
