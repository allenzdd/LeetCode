# class Solution:
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = []
#         for i in range(2 ** len(nums)):
#             comb = []
#             for j in range(len(nums)):
#                 if (i >> j) % 2 == 1:
#                     comb.append(nums[j])
#             res.append(comb)

#         return res


# More faster

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for x in nums:
            res += [j + [x] for j in res]
        return res


nums = [1, 2, 3]
print(Solution().subsets(nums))
