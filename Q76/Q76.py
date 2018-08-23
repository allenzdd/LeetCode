class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_dict_1 = {}
        s_dict_2 = {}
        for x in t:
            if x not in s_dict_1:
                s_dict_1[x] = 0
                s_dict_2[x] = 0
            s_dict_1[x] += 1
            s_dict_2[x] += 1

        left = 0
        min_len = len(s) + 1
        count = len(t)
        min_left = 0

        for right in range(len(s)):
            if s[right] in s_dict_1:
                s_dict_2[s[right]] -= 1
                if s_dict_2[s[right]] >= 0:
                    count -= 1
                if count == 0:
                    while True:
                        if s[left] in s_dict_2:
                            if s_dict_2[s[left]] < 0:
                                s_dict_2[s[left]] += 1
                            else:
                                break
                        left += 1
                    if right - left + 1 < min_len:
                        min_len = right - left + 1
                        min_left = left
        if min_len < len(s) + 1:
            return s[min_left:min_left + min_len]
        else:
            return ""


S = "ADOBECODEBANC"
T = "AB"
print(Solution().minWindow(S, T))
