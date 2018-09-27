# Trie Tree
# DFS
class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # generate tire tree
        dic = {}
        for word in words:
            p = dic
            for ch in word:
                if ch not in p:
                    p[ch] = {}
                p = p[ch]
            p["#"] = True
        # init dfs
        self.h = len(board)
        self.w = len(board[0])
        self.res = []
        self.board = board
        # start dfs
        for i in range(self.h):
            for j in range(self.w):
                visited = [[False] * self.w for _ in range(self.h)]
                if board[i][j] in dic:
                    self.dfs(i, j, dic[board[i][j]], board[i][j], visited)
        return self.res

    def dfs(self, i, j, sub_dic, prefix, visited):
        if '#' in sub_dic and prefix not in self.res:
            self.res.append(prefix)
        visited[i][j] = True
        board = self.board
        if i+1<self.h:
            if board[i+1][j] in sub_dic and not visited[i+1][j]: 
                self.dfs(i+1, j, sub_dic[board[i+1][j]], prefix+board[i+1][j], visited)
                visited[i+1][j] = False
        if i-1>=0:
            if board[i-1][j] in sub_dic and not visited[i-1][j]:
                self.dfs(i-1, j, sub_dic[board[i-1][j]], prefix+board[i-1][j], visited)
                visited[i-1][j] = False
        if j-1>=0:
            if board[i][j-1] in sub_dic and not visited[i][j-1]: 
                self.dfs(i, j-1, sub_dic[board[i][j-1]], prefix+board[i][j-1], visited)
                visited[i][j-1] = False
        if j+1<self.w:
            if board[i][j+1] in sub_dic and not visited[i][j+1]:
                self.dfs(i, j+1, sub_dic[board[i][j+1]], prefix+board[i][j+1], visited)
                visited[i][j+1] = False
        





# words = ["oath","pea","eat","rain"]

# board = [['o','a','a','n'],
#         ['e','t','a','e'],
#         ['i','h','k','r'],
#         ['i','f','l','v']]

board = [["b","a","a","b","a","b"],
    ["a","b","a","a","a","a"],
    ["a","b","a","a","a","b"],
    ["a","b","a","b","b","a"],
    ["a","a","b","b","a","b"],
    ["a","a","b","b","b","a"],
    ["a","a","b","a","a","b"]]

words = ["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba",
    "babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa",
    "babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa",
    "babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba",
    "aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba",
    "ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab",
    "aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa",
    "aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa",
    "abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb",
    "aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb",
    "aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa",
    "abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab",
    "aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba",
    "aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb",
    "aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]



print(Solution().findWords(board, words))