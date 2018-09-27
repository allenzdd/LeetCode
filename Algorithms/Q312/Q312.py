class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        opt = [[0] * len(nums) for _ in range(len(nums))]
        for length in range(1, len(nums)-1):
            for i in range(1, len(nums)-length):
                j = i + length - 1
                for k in range(i, j+1):
                    opt[i][j] = max(opt[i][j], opt[i][k-1] + nums[i-1]*nums[k]*nums[j+1] + opt[k+1][j])
        return opt[1][len(nums)-2]


nums = [3,1,5,8]
print(Solution().maxCoins(nums))