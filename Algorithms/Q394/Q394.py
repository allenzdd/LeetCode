# Stack
# 36ms
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [["", 1]]
        num = ""
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == "[":
                stack.append(["", int(num)])
                num = ""
            elif ch == "]":
                c_sub, k = stack.pop()
                stack[-1][0] += c_sub * k
            else:
                stack[-1][0] += ch
        return stack[-1][0]


# s = "3[a]2[bc]"
s = "2[abc]3[cd]ef"
print(Solution().decodeString(s))