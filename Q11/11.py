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

        x = len(height) - 1

        y = 0

        while x != y:
        	if height[x] > height[y]:
        		area = height[y] * (x - y)
        		y += 1
        	else:
        		area = height[x] * (x - y)

        	MAX = max(MAX, area)
        
        return MAX


Run = Solution()

height = [1, 2]

result = Run.maxArea(height)

print(result)