# Math Method
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int((sum(nums) - sum(set(nums))) / (len(nums) - len(set(nums))))



# # binary search
# class Solution:
#     def findDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         low, high = 0, len(nums) - 1
#         mid = (low + high) // 2
#         while high - low > 1:
#             count = 0
#             for num in nums:
#                 if mid < num <= high:
#                     count += 1
#             if count > high - mid:
#                 low = mid
#             else:
#                 high = mid
#             mid = (low + high) // 2
#         return high

nums = [1,3,4,2,2]
print(Solution().findDuplicate(nums))