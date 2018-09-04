# class Solution:
#     def lengthOfLIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#         opt = [1] * len(nums)
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     opt[i] = max(opt[i], opt[j] + 1)
#         return max(opt)


# Second Method O(nlogn)
class Solution:
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size


# nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
print(Solution().lengthOfLIS(nums))
