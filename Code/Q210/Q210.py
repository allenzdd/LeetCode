class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.res = []
        graph = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[y].append(x)

        self.stack = [False] * numCourses
        self.visited = [False] * numCourses

        for i in range(numCourses):
            if not self.visited[i]:
                if self.dfs(graph, i, numCourses):
                    return self.res
        
    def dfs(self, graph, i, numCourses):
        self.stack[i] = True
        self.visited[i] = True
        self.res.append(i)
        for j in graph[i]:
            if not self.visited[j]:
                self.dfs(graph, j, numCourses)
        

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# numCourses = 2
# prerequisites = [[0,1]]
print(Solution().findOrder(numCourses, prerequisites))