class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = ["()"]
        for temp in range(1, n):
            res = list(set([x[0:k] + "()" + x[k:]
                            for x in res for k in range(len(res) + 1)]))
        return res


n = 4

res = Solution().generateParenthesis(n)

print(res)
