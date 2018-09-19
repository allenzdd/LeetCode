class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x

        while l <= r:
            t = (l + r) // 2
            if t ** 2 <= x < (t+1) ** 2:
                return t
            elif t**2 > x:
                r = t - 1
            else:
                l = t + 1
        return False

print(Solution().mySqrt(9))
