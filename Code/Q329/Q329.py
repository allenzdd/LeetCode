class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # h = len(matrix)
        # w = len(matrix[0])
        longest = 0
        self.memory = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp_len = self.dfs(i, j, matrix)
                longest = max(temp_len, longest)
        return longest
    
    def dfs(self, i, j, matrix):
        if self.memory[i][j]:
            return self.memory[i][j]
        h = len(matrix)
        w = len(matrix[0])
        count = 0
        temp = matrix[i][j]
        if i+1 < h and matrix[i+1][j] < temp:
            count = max(count, self.dfs(i+1, j, matrix))
        if i-1 >= 0 and matrix[i-1][j] < temp:
            count = max(count, self.dfs(i-1, j, matrix))
        if j+1 < w and matrix[i][j+1] < temp:
            count = max(count, self.dfs(i, j+1, matrix))
        if j-1 >= 0 and matrix[i][j-1] < temp:
            count = max(count, self.dfs(i, j-1, matrix))
        self.memory[i][j] = count + 1
        return count+1



# nums = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 

print(Solution().longestIncreasingPath(nums))



# # TLE
# # DFS
# class Solution:
#     def longestIncreasingPath(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: int
#         """
#         self.longest = 0
#         self.h = len(matrix)
#         self.w = len(matrix[0])

#         for i in range(self.h):
#             for j in range(self.w):
#                 visited = [[False] * self.w for _ in range(self.h)]
#                 temp_long = 0
#                 self.dfs(i, j, matrix, temp_long, visited)
#         return self.longest

#     def dfs(self, i, j, matrix, temp_long, visited):
#         temp_long += 1
#         visited[i][j] = True
#         temp = matrix[i][j]
#         if i+1 < self.h:
#             if matrix[i+1][j] < temp and not visited[i+1][j]:
#                 self.dfs(i+1, j, matrix, temp_long, visited)
#                 self.longest = max(temp_long+1, self.longest)
#                 visited[i+1][j] = False
#         if i-1 >= 0:
#             if matrix[i-1][j] < temp and not visited[i-1][j]:
#                 self.dfs(i-1, j, matrix, temp_long, visited)
#                 self.longest = max(temp_long+1, self.longest)
#                 visited[i-1][j] = False
#         if j+1 < self.w:
#             if matrix[i][j+1] < temp and not visited[i][j+1]:
#                 self.dfs(i, j+1, matrix, temp_long, visited)
#                 self.longest = max(temp_long+1, self.longest)
#                 visited[i][j+1] = False
#         if j-1 >= 0:
#             if matrix[i][j-1] < temp and not visited[i][j-1]:
#                 self.dfs(i, j-1, matrix, temp_long, visited)
#                 self.longest = max(temp_long+1, self.longest)
#                 visited[i][j-1] = False