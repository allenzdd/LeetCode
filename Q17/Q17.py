class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict_digits = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pdrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        prev = dict_digits[digits[0]]
        i = 1
        while i < len(digits):
            prev = self.append_fun(prev, dict_digits[digits[i]])
            i += 1
        return prev

    def append_fun(self, previous, current):
        res = []
        for i in range(len(previous)):
            for cur in current:
                res.append(previous[i] + cur)
        return res


digits = '234'
res = Solution().letterCombinations(digits)
print(res)
