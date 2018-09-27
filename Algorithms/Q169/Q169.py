class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        for num in set_nums:
            if nums.count(num) > len(nums) / 2:
                return num
        return 

nums = [3,2,3]
print(Solution().majorityElement(nums))