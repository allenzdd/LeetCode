class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)

        opt = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    opt[i][j] = j
                elif j == 0:
                    opt[i][j] = i
                else:
                    if word1[i - 1] == word2[j - 1]:
                        same = 0
                    else:
                        same = 1
                    opt[i][j] = min(opt[i - 1][j - 1] + same,
                                    min(opt[i - 1][j], opt[i][j - 1]) + 1
                                    )
        # print(opt)
        return opt[-1][-1]


word1 = 'intention'
word2 = 'execution'

# word1 = ""
# word2 = ""

# word1 = "a"
# word2 = "ab"

print(Solution().minDistance(word1, word2))
