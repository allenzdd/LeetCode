# import itertools


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # comb = itertools.combination
        comb = [float('Nan') for _ in range(n)]

        # input = 1
        comb[0] = 1

        if n > 1:
            # input = 2
            comb[1] = 2

        # comb[2] = comb[1] + comb[2]
        if n > 2:
            for i in range(2, n):
                comb[i] = comb[i - 2] + comb[i - 1]

        return comb[n - 1]


n = 2

print(Solution().climbStairs(n))
