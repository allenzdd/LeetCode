# DFS
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """        
        # check number of invalid-()
        l, r = 0, 0
        for i in range(len(s)):
            l += (s[i] == '(')
            if l == 0:
                r += (s[i] == ')')
            else:
                l -= (s[i] == ')')
        res = []
        visited = set()
        self.dfs(s, 0, l, r, res, visited)
        return res

    # judge the string validation
    def is_valid(self, s):
        count = 0
        for s_i in s:
            if s_i == '(':
                count += 1
            if s_i == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0
          
    def dfs(self, s, start, l, r, res, visited):
        # if visited exist the calculation has been run
        if s not in visited:
            visited.add(s)
        else:
            return
        # judge the s whether append 
        if l == 0 and r == 0:
            if self.is_valid(s):
                res.append(s)
            else:
                return         
        # DFS main
        for i in range(len(s)):
            if i != start and s[i] == s[i - 1]:
                continue
            elif s[i] in ('(', ')'):
                temp = s[:i] + s[i+1:]
                # judge ()
                if s[i] == '(' and l > 0:
                    self.dfs(temp, i, l - 1, r, res, visited)
                elif s[i] == ')' and r > 0:
                    self.dfs(temp, i, l, r - 1, res, visited)
  


# s = '()())()'
# s = '()'
# s = "(a)())()"
# s = ')('
# s = ")()(e()))))))(((("
s = ")k)))())()())))())"
print(Solution().removeInvalidParentheses(s))