class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1

        diffPath = [[0] * n] * m

        for i in range(m):
            diffPath[i][0] = 1

        for j in range(n):
            diffPath[0][j] = 1

        for row in range(1, m):
            for col in range(1, n):
                diffPath[row][col] = diffPath[row][col - 1] + \
                    diffPath[row - 1][col]

        return diffPath[-1][-1]


m = 7
n = 3

print(Solution().uniquePaths(m, n))
