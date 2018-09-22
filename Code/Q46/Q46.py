# DFS
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        self.dfs(nums, temp, res)
        return res
        
    def dfs(self, nums, temp, res):
        if len(nums) == len(temp):
            res.append(temp[:])
            return 
        
        for num in nums:
            if num in temp:
                continue
            temp.append(num)
            self.dfs(nums, temp, res)
            # pop temp last element becuase in order to next element recursion
            temp.pop()








nums = [1, 2, 3, 4]
res = Solution().permute(nums)
print(res)


# # insert method
# class Solution:
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = [[]]
#         for x in nums:
#             temp = []
#             for res_i in res:
#                 for i in range(len(res_i) + 1):
#                     temp.append(res_i[:i] + [x] + res_i[i:])
#             res = temp
#             print(x)
#             print(res)
#         return res

# nums = [1, 2, 3, 4]
# res = Solution().permute(nums)
# print(res)
