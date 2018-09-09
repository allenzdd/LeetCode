class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        # implement sliding windows as follow:
        # opt = [0] * len(nums)
        opt = [0] * 2
        opt[0] = nums[0]
        opt[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            temp = opt[(i - 2) % 2] + nums[i]
            opt[i % 2] = max(temp, opt[(i - 1) % 2])
        # because sliding windows so shoudn't use opt[-1] but max(opts)
        return max(opt)

nums = [2,7,9,3,1]
print(Solution().rob(nums))
        