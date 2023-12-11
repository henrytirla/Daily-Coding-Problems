"""Given a Roman numeral, write a program to find its corresponding decimal value. Roman numerals are represented by seven different symbols:

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
Problem Note
The input contains only the characters 'I', 'V', 'X', 'L', 'C', 'D', 'M'.
Input is a valid roman numeral in the range [1, 3999].
A number in Roman numerals is a string of these symbols written in descending order i.e. largest to smallest from left to right. For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is XXVII, which is XX + V + II.
We avoid four characters being repeated in successions such as IIII or VIIII. Instead, the number four is written as IV because the 1 is before the 5, and we subtract it making 4. The same principle applies to number 9, which is written as IX. The idea is: when there is a smaller number placed before a larger number, the values are subtracted.



Example 1: Input: XL, Output: 40

Explanation: XL is a Roman symbol which represents 40

Example 2: Input: MCMIV, Output: 1904
"""

def test_roman_Decimal():
    sol= Solution()

    assert sol.roman_Decimal("XL") == 40
    assert sol.roman_Decimal("LX")== 60


class Solution:
    def roman_Decimal(self,romanstring:str)-> int:
        roman_dict={"I": 1,"V":5,"X":10,"L":50, "C":100,"D":500,"M":1000}

        pass