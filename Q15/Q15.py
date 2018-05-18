import itertools
import numpy as np
class Solution:
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		zero_list = []
		for x in itertools.combinations(nums, 3):
			if np.sum(x) == 0:
				x = sorted(x)
				if x not in zero_list:
					zero_list.append(x)
		return zero_list

nums = [-1, 0, 1, 2, -1, -4]

res = Solution().threeSum(nums)

print(res)