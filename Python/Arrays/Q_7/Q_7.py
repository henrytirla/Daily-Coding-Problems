"""

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

Useful resources
https://leetcode.com/problems/group-anagrams/


Solution Explanation
https://www.youtube.com/embed/vzdNOK2oB2E

"Understand ORD fucntion and what it does"
https://www.youtube.com/watch?v=NfwArODGWHE

"Understand Defautl Dict"
https://www.geeksforgeeks.org/defaultdict-in-python/
"""

from collections import defaultdict



def GroupAnagram(str):
    res = defaultdict(list)
    for s in str:
        count= [0] * 26
        for c in s:
            count[ord(c)-ord("a")] +=1
        res[tuple(count)].append(s)
    return res.values()

str = ["eat","tea","tan","ate","nat","bat"]


if __name__ == '__main__':
    print(list(GroupAnagram(str)))
















