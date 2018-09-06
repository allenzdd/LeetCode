class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        opt = [False] * (n + 1)
        opt[0] = True
        for i in range(n + 1):
            for j in range(i, n + 1):
                if s[i:j] in wordDict and opt[i] == True:
                    opt[j] = True
                    # break
        return opt[-1]

# s = 'leetcode'
# wordDict = ['leet', 'code']

s = "aaaaaaa"
wordDict = ["aaaa","aaa"]

print(Solution().wordBreak(s, wordDict))