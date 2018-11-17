# Manacher Algorithm
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = "$#" + "#".join(s) + "#+"
        RL = [0] * len(t)
        pos, max_right, max_len, max_len_pos = 0, 0, 0, 0
        for i in range(1, len(t)-1):
            if max_right > i:
                RL[i] = min(RL[2*pos - i], max_right-i)
            else:
                RL[i] = 1
            while t[i - RL[i]] == t[i + RL[i]]:
                RL[i] += 1
            if i + RL[i] > max_right:
                max_right = i + RL[i]
                pos = i
            if RL[i] > max_len:
                max_len = RL[i]
                max_len_pos = i
        return s[(max_len_pos - max_len) // 2: (max_len_pos - max_len) // 2 + max_len - 1]
                



# DP
class Solution_DP:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        opt = [[0] * len(s) for _ in range(len(s))]
        max_len = 0
        res = ""
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 3 or opt[i+1][j-1]==1):
                    opt[i][j] = 1
                    if res == "" or max_len < j - i + 1:
                        res = s[i:j+1]
                        max_len = j - i + 1
        return res


if __name__ == "__main__":
    # s = 'abaaaba'
    s = "babad"
    res = Solution().longestPalindrome(s)
    print(res)