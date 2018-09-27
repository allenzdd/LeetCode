# DFS
class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:   return 
        keep = []
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if i in (0, m-1) or j in (0, n-1):
                    self.dfs(i, j, board, keep, m, n)
        for i in range(m):
            for j in range(n):
                if [i, j] not in keep and board[i][j] == "O":
                    board[i][j] = "X"
        
    
    def dfs(self, i, j, board, keep, m, n):
        if board[i][j] == "O" and [i, j] not in keep:
            keep.append([i, j])
            if m > i >= 1 and 0 <= j < n:
                self.dfs(i-1, j, board, keep, m, n)
            if 0 <= i <= m - 2 and 0 <= j < n:
                self.dfs(i+1, j, board, keep, m, n)
            if 0 <= i < m and n > j >= 1:
                self.dfs(i, j-1, board, keep, m, n)
            if 0 <= i < m and 0 <= j <= n - 2:
                self.dfs(i, j+1, board, keep, m, n)
        else:
            return 

# board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# board = [["X", "X"], ["O", "X"]]
board = [["X","O","O","X","X","X","O","X","O","O"],
        ["X","O","X","X","X","X","X","X","X","X"],
        ["X","X","X","X","O","X","X","X","X","X"],
        ["X","O","X","X","X","O","X","X","X","O"],
        ["O","X","X","X","O","X","O","X","O","X"],
        ["X","X","O","X","X","O","O","X","X","X"],
        ["O","X","X","O","O","X","O","X","X","O"],
        ["O","X","X","X","X","X","O","X","X","X"],
        ["X","O","O","X","X","O","X","X","O","O"],
        ["X","X","X","O","O","X","O","X","X","O"]]

Solution().solve(board)
print(board)