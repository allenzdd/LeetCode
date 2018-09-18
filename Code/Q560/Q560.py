class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = pre_sum = 0
        dic = {0:1}
        for num in nums:
            pre_sum += num
            res += dic.get(pre_sum - k, 0)
            dic[pre_sum] = dic.get(pre_sum, 0) + 1
        return res



nums = [1,1,1]
k = 2
print(Solution().subarraySum(nums, k))



# # TLE
# class Solution:
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         res = 0
#         for i in range(len(nums)):
#             j = i + 1
#             while True:
#                 if j > len(nums):
#                     break
#                 if sum(nums[i:j]) == k:
#                     res += 1
#                 j += 1
#         return res