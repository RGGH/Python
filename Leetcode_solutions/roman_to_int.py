# Input: s = "III"
# Output: 3

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4

# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

class Solution:

    def __init__(self):
        self.nums = {"I": 1, "V": 5, "X": 10,
                     "L": 50, "C": 100, "D": 500, "M": 1000}

    def romanToInt(self, s: str):

        # tally of the exceptions
        tally = 0

        if 'IV' in s:
            tally += 4
            s = s.replace("IV", '')

        if 'IX' in s:
            tally += 9
            s = s.replace("IX", '')

        if 'XL' in s:
            tally += 40
            s = s.replace("XL", '')

        if 'XC' in s:
            tally += 90
            s = s.replace("XC", '')

        if 'CD' in s:
            tally += 400
            s = s.replace("CD", '')

        if 'CM' in s:
            tally += 900
            s = s.replace("CM", '')

        # sum of roman numerals once exceptions removed
        roman = 0

        for i in s:
            if i in self.nums.keys():
                roman += (self.nums[i])

        z = (roman+tally)
        return z


test = Solution()
test = test.romanToInt("IX")
print(test)
