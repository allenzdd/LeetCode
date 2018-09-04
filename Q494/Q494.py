class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        res = {nums[0]:1, -nums[0]:1} if nums[0] != 0 else {0:2}
        print(res)

        for i in range(1, len(nums)):
            x = nums[i]
            temp = {}
            for t in res:
                temp[t + x] = temp.get(t + x, 0) + res.get(t, 0)
                temp[t - x] = temp.get(t - x, 0) + res.get(t, 0)
            res = temp
        return res.get(S, 0)
        


nums = [1, 1, 1, 1, 1]
S = 3

# nums = [0,0,0,0,0,0,0,0,1]
# # nums = [0,0,1]
# S = 1

# nums = [25,33,27,23,46,16,10,27,33,2,12,2,29,44,49,40,32,46,7,50]
# S = 4
print(Solution().findTargetSumWays(nums,S))


# class Solution:
#     def findTargetSumWays(self, nums, S):
#         """
#         :type nums: List[int]
#         :type S: int
#         :rtype: int
#         """
#         res = [nums[0], -nums[0]]

#         if len(nums) == 1:
#             temp = 0
#             for x in res:
#                 if x == S:
#                     temp += 1
#             return temp

#         if not nums:
#             return 0
            
#         for x in nums[1:]:
#             temp = []
#             for y in res:
#                 temp.append(y + x)
#                 temp.append(y - x)
#             res = temp        
#         return res.count(S)