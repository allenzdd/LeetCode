class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True

    def dfs(self, graph, visited, i):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        
        visited[i] = -1
        
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        
        visited[i] = 1
        return True

num = 2
prereq = [[1,0],[0,1]]

print(Solution().canFinish(num, prereq))