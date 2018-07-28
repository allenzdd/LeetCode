class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        maxThreeInt = 3**19

        return n > 0 and maxThreeInt % n == 0


n = -3
res = Solution().isPowerOfThree(n)
print(res)
