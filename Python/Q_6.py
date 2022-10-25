"""

Given two strings s and t, return true if t is an anagram of s,
and false otherwise.

An Anagram is a word or phrase formed by
rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

 Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters?
How would you adapt your solution to such a case?

Useful Resource
https://www.youtube.com/embed/9UtInBqnCgA

To understand -> (function annotation)
https://stackoverflow.com/questions/14379753/what-does-mean-in-python-function-definitions
https://peps.python.org/pep-3107/
"""

def checkAnagram(s,t) -> bool:
    if len(s) != len(t):
        return False
    CountS,CountT = {}, {}
    for i in range(len(s)):
        CountS[s[i]] = 1+ CountS.get(s[i],0)
        CountT[t[i]] = 1+ CountT.get(t[i],0)
    for c in CountS:
        if CountS[c] != CountT.get(c,0):
            return False
    return  True




s = "anagram"
t= "nagaran"

print(checkAnagram(s,t))

