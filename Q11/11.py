'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        MAX = 0

        x = 0

        y = len(height) - 1

        while x != y:
            for i in range(x + 1, len(height)):
                if height[x] > height[i]:
                    area = height[i] * (i - x)
                else:
                    area = height[x] * (i - x)
                MAX = max(MAX, area)
            # if height[x] > height[y]:
            #     area = height[y] * (y - x)
            # else:
            #     area = height[x] * (y - x)

            # MAX = max(MAX, area)
            x += 1

        return MAX


Run = Solution()

height = [2, 3, 4, 5, 18, 17, 6]

result = Run.maxArea(height)

print(result)
