class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, water, minHeight = 0, len(height) - 1, 0, 0
        while left < right:
            while left < right and height[left] <= minHeight:
                water += minHeight - height[left]
                left += 1
            while right > left and height[right] <= minHeight:
                water += minHeight - height[right]
                right -= 1
            minHeight = min(height[left], height[right])

        return water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(Solution().trap(height))
