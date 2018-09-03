class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    res += 1
        return res

    def dfs(self, grid, i, j):
        grid[i][j] = '0'
        if grid[i][j - 1] == '1' and j - 1 >= 0:
            self.dfs(grid, i, j - 1)
        if grid[i - 1][j] == '1' and i - 1 >= 0:
            self.dfs(grid, i - 1, j)
        if j + 1 < len(grid[0]) and grid[i][j + 1] == '1':
            self.dfs(grid, i, j + 1)
        if i + 1 < len(grid) and grid[i + 1][j] == '1':
            self.dfs(grid, i + 1, j)


# grid = [['1', '1', '1', '1', '0'],
#         ['1', '1', '0', '1', '0'],
#         ['1', '1', '0', '0', '0'],
#         ['0', '0', '0', '0', '0']]


grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]

print(Solution().numIslands(grid))
