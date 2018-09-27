class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_index], nums[i] = nums[i], nums[zero_index]
                zero_index += 1


# # TLE
# class Solution:
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         count_zero = nums.count(0)
#         i = 0
#         while nums[:len(nums) - count_zero].count(0) > 0:
#             if nums[i] != 0:
#                 i += 1
#             else:
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]


nums = [0,1,0,3,12]
nums = [0,1,0]
# print(Solution().moveZeroes(nums))
Solution().moveZeroes(nums)
print(nums)