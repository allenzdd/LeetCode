class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict_char = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in dict_char.values():
                stack.append(char)
            elif char in dict_char.keys():
                if stack == [] or dict_char[char] != stack.pop():
                    return False

        return stack == []


s = "[]"

res = Solution().isValid(s)

print(res)
