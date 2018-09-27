class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length = len(needle)
        if needle != "":
            for i in range(0, len(haystack) - length + 1):
                if haystack[i: (i + length)] == needle:
                    return i

            return -1
        elif needle == "":
            return 0


haystack = "aaaaab"
needle = ""
res = Solution().strStr(haystack, needle)

print(res)
