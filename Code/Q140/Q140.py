class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # init dp
        opt = [[] for _ in range(len(s) + 1)]
        opt[0] = [0]
        # implement dp
        for i in range(1, len(s)+1):
            for j in range(i):
                if opt[j] and s[j:i] in wordDict:
                    opt[i].append(j)
        # backtrack
        res = []
        self.backtrack(opt, s, len(s), res, '')
        return res
    
    def backtrack(self, opt, s, idx, res, line):
        for i in opt[idx]:
            newline = s[i:idx] + ' ' + line if line else s[i:idx]
            if i == 0:
                res.append(newline)
            else:
                self.backtrack(opt, s, i, res, newline)

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]

print(Solution().wordBreak(s, wordDict))
