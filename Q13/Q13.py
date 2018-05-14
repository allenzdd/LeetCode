class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        roman_dict = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90, \
                            'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}

        while len(s) != 0:
            if s[:2] in roman_dict:
                res += roman_dict[s[:2]]
                s = s[2:]
            elif s[:1] in roman_dict:
                res += roman_dict[s[:1]]
                s = s[1:]

        return res

s = "MCMXCIV"

result = Solution().romanToInt(str(s))
print(result)