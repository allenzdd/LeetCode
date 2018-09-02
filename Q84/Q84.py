class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 1:
            return heights[0]
        if not heights:
            return 0
        stack = []
        res = 0
        heights.append(-1)
        for i in range(len(heights)):
            current = heights[i]
            while len(stack) != 0 and current <= heights[stack[-1]]:
                h = heights[stack.pop()]
                if len(stack) == 0:
                    w = i
                else:
                    w = i - stack[-1] - 1
                res = max(res, w * h)
            stack.append(i)
        return res


# heights = [2, 1, 5, 6, 2, 3]
# heights = [0]
heights = [1, 1]
print(Solution().largestRectangleArea(heights))
