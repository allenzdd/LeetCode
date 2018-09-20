# string
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                temp = s[i:j]
                if temp == temp[::-1]:
                    res += 1
        return res

print(Solution().countSubstrings('abc'))