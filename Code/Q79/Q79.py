class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                res = self.dfs(board, word, i, j, 0)
                if res:
                    return True
        return False

    def dfs(self, board, word, mx, ny, d):
        if mx < 0 or ny < 0 or mx >= self.m or ny >= self.n or board[mx][ny] != word[d]:
            return False
        if d == len(word) - 1:
            return True

        temp = board[mx][ny]
        board[mx][ny] = 0
        res = False
        res = self.dfs(board, word, mx + 1, ny, d + 1) or \
            self.dfs(board, word, mx, ny + 1, d + 1) or \
            self.dfs(board, word, mx - 1, ny, d + 1) or \
            self.dfs(board, word, mx, ny - 1, d + 1)
        board[mx][ny] = temp
        return res


# board = [
#     ['A', 'B', 'C', 'E'],
#     ['S', 'F', 'C', 'S'],
#     ['A', 'D', 'E', 'E']
# ]

# word = "ABCCED"

board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
word = "AAB"
print(Solution().exist(board, word))
