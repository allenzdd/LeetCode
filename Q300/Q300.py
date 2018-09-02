class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        opt = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    opt[i] = max(opt[i], opt[j] + 1)
        return max(opt)


# nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
print(Solution().lengthOfLIS(nums))
