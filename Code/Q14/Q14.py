class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix_len = 0
        for x in zip(*strs):
        	if len(set(x)) == 1:
        		prefix_len += 1
        	else:
        		break
        if prefix_len != 0:
        	return strs[0][:prefix_len]
        else:
        	return ""


strs = ["flaower","flaow","flaight"]

res = Solution().longestCommonPrefix(strs)
print(res)