
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[0:3])
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                dist_temp = abs(temp - target)
                dist_res = abs(res - target)
                if temp == target:
                    return temp
                elif dist_temp < dist_res:
                    res = temp

                if temp < target:
                    j += 1
                elif temp > target:
                    k -= 1
        return res


# class Solution:
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         count = {}
#         for i in nums:
#             count[i] = count.get(i, 0) + 1

#         nsort = sorted(count.keys())

#         if len(nsort) == 1:
#             return nsort[0] * 3
#         elif len(nsort) == 2:
#             for i in range(2):
#             	n1 = nsort[i]
#             	if count[n1] >= 1:
#             		count[n1] -= 1
#             		for j in range(1, 2):
#         	############# Old Method ##############
#             # n1 = nsort[0]
#             # n2 = nsort[1]
#             # if count[n1] >= 2 and count[n2] == 1:
#             #     temp_sum = n1 * 2 + n2
#             #     return temp_sum
#             # elif count[n1] == 1 and count[n2] >= 2:
#             #     temp_sum = n1 + n2 * 2
#             #     return temp_sum
#             # else:
#             #     temp_sum1 = n1 * 2 + n2
#             #     temp_sum2 = n1 + n2 * 2
#             #     if abs(target - temp_sum1) < abs(target - temp_sum2):
#             #         return temp_sum1
#             #     else:
#             #         return temp_sum2
#         else:
#             temp_close = abs(sum(nsort[:3]))
#             res = sum(nsort[:3])

#             for i in range(len(nsort)):
#                 n1 = nsort[i]
#                 if count[n1] >= 1:
#                     count[n1] -= 1
#                     for j in range(i + 1, len(nsort)):
#                         n2 = nsort[j]
#                         if count[n2] >= 1:
#                             count[n2] -= 1
#                             for k in range(j + 1, len(nsort)):
#                                 n3 = nsort[k]
#                                 if count[n3] >= 1:
#                                     count[n3] -= 1
#                                     temp_sum = n1 + n2 + n3
#                                     temp = abs(target - temp_sum)
#                                     if temp < temp_close:
#                                         temp_close = temp
#                                         res = temp_sum
#                                 count[n3] += 1
#                         count[n2] += 1
#                 count[n1] += 1
#             return res


# # Second Method --- time exceeded
# import itertools
# class Solution:
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         temp_close = abs(target - sum(nums[:3]))
#         res = sum(nums[:3])
#         for x in itertools.combinations(nums, 3):
#             temp = abs(target - sum(x))
#             if temp < temp_close:
#                 temp_close = temp
#                 res = sum(x)
#         return res


# nums = [-1, 2, 1, -4, 2, 6]
# nums = [0, 0, 0]
nums = [0, 1, 2]
target = 0

res = Solution().threeSumClosest(nums, target)

print(res)
