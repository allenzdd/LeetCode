class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum = -float('inf')
        maxSum = -float('inf')
        for x in nums:
            currSum = max(x, currSum + x)
            maxSum = max(maxSum, currSum)
        return maxSum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(Solution().maxSubArray(nums))
