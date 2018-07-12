class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        temp = divisor
        i = 0
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                temp <<= 1
                i <<= 1
                temp *= 2
                # i *= 2
        if not positive:
            res = -res
        return min(max(-2**31, res), 2**31 - 1)


dividend = 1000032
divisor = 2
res = Solution().divide(dividend, divisor)
print(res)