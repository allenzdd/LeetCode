class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        opt = [1]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                temp = opt[-1] + 1
                opt.append(temp)
            elif nums[i] == nums[i - 1]:
                opt.append(opt[i - 1])
            else:
                opt.append(1)
        return max(opt)


# nums = [100, 4, 200, 1, 3, 2]
nums = [1, 2, 0, 1]
print(Solution().longestConsecutive(nums))
