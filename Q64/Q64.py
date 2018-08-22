class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        opt = [[float('inf') for _ in range(n)] for _ in range(m)]

        opt[0][0] = grid[0][0]

        for col in range(1, n):
            opt[0][col] = opt[0][col - 1] + grid[0][col]

        for row in range(1, m):
            opt[row][0] = opt[row - 1][0] + grid[row][0]

        for row in range(1, m):
            for col in range(1, n):
                opt[row][col] = min(opt[row - 1][col],
                                    opt[row][col - 1]) + grid[row][col]

        return opt[-1][-1]


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

print(Solution().minPathSum(grid))
