# BFS
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        lst = []
        while i * i <= n:
            if i * i == n:
                return 1
            lst.append(i * i)
            i += 1
        
        nodes = {n}
        depth = 1
        while True:
            next_level = set()
            for node in nodes:
                for x in lst:
                    if node == x:
                        return depth
                    if node < x:
                        break
                    next_level.add(node - x)
            depth += 1
            nodes = next_level
        return depth

n = 12
print(Solution().numSquares(n))