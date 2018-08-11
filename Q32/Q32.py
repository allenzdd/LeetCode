class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        opt = [0 for _ in range(len(s))]

        max_temp = 0

        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":
                    # print(i)
                    opt[i] = opt[i - 2] + 2
                elif i - opt[i - 1] - 1 >= 0 and s[i - opt[i - 1] - 1] == "(":
                    # print(i)
                    if opt[i - 1] > 0:
                        opt[i] = opt[i - 1] + 2 + opt[i - opt[i - 1] - 2]
                        # print(opt)
                    else:
                        opt[i] = 0
                        # print(opt)
                max_temp = max(max_temp, opt[i])

        return max_temp


s = "()(())"
print(Solution().longestValidParentheses(s))
