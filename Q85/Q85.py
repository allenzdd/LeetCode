class Solution:
    def maximalRectangle(self, matrix):
        """
		:type matrix: List[List[str]]
		:rtype: int
		"""
        if len(matrix) == 0:
            return 0
        heights = [0] * len(matrix[0]) + [-1]
        res = 0
        for i in range(len(matrix)):
            temp_h = list(map(int, matrix[i])) + [-1]
            stack = []
            for j in range(len(temp_h)):
                if temp_h[j] == 1:
                    temp_h[j] += heights[j]
                current = temp_h[j]
                while len(stack) != 0 and current <= temp_h[stack[-1]]:
                    h = temp_h[stack.pop()]
                    if len(stack) == 0:
                        w = j
                    else:
                        w = j - stack[-1] - 1
                    res = max(res, w * h)
                stack.append(j)
            heights = temp_h
        return res


mat = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]

# mat = [["0","0","1","0"],
# 		["1","1","1","1"],
# 		["1","1","1","1"],
# 		["1","1","1","0"],
# 		["1","1","0","0"],
# 		["1","1","1","1"],
# 		["1","1","1","0"]]
print(Solution().maximalRectangle(mat))

# class Solution:
#     def maximalRectangle(self, matrix):
#         """
#         :type matrix: List[List[str]]
#         :rtype: int
#         """
#         heights = [list(map(int, matrix[0]))]
#         for i in range(1, len(matrix)):
#             temp_h = list(map(int, matrix[i]))
#             for j in range(len(temp_h)):
#                 if temp_h[j] == 1:
#                     temp_h[j] += heights[-1][j]
#             heights.append(temp_h)
#         # print(heights)
