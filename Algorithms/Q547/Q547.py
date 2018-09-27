class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = [False] * len(M)
        res = 0
        for i in range(len(M)):
            if not visited[i]:
                self.dfs(M, i, visited)
                res += 1
        return res

    def dfs(self, M, i_pre, visited):
        visited[i_pre] = True
        for j in range(len(M)):
            if not visited[j]:
                if M[i_pre][j] == 1:
                    self.dfs(M, j, visited)


M = [[1, 1, 0],
     [1, 1, 0],
     [0, 0, 1]]

print(Solution().findCircleNum(M))
