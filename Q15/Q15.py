import itertools
import numpy as np

# # First Method
# class Solution:
# 	def threeSum(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: List[List[int]]
# 		"""
# 		zero_list = []
# 		nums.sort()
# 		for x in itertools.combinations(nums, 3):
# 			if np.sum(x) == 0:
# 				# x = sorted(x)
# 				if x not in zero_list:
# 					zero_list.append(x)
# 		return zero_list

# # Second Method O(n^2)
# class Solution:
# 	def threeSum(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: List[List[int]]
# 		"""
# 		if len(nums) < 3:
# 			return []
# 		elif len(nums) == 3:
# 			if sum(nums) == 0:
# 				return [nums]
# 		else:
# 			nums.sort()
# 			res = []
# 			for i in range(len(nums) - 2):
# 				j = i + 1
# 				k = len(nums) - 1

# 				while j < k:
# 					temp = (nums[i], nums[j], nums[k])
# 					temp_sum = np.sum(temp)
# 					if temp_sum == 0:
# 						res.append(temp)
# 					elif temp_sum > 0:
# 						j += 1
# 					else:
# 						k -= 1
# 			return res

# Third Method
class Solution:
    def threeSum(self, nums):
        count={} # number: count
        for i in nums:
            count[i] = count.get(i,0) + 1

        ans = []
        nsort = sorted(count.keys())

        for i in range(len(nsort)):
            n1 = nsort[i]
            count[n1] -= 1
            for j in range(i,len(nsort)):
                n2 = nsort[j]
                if count[n2] >= 1:
                    count[n2] -= 1
                    n3 = - (n1 + n2)
                    if n3>=n2 and n3 in count and count[n3]>=1:
                        ans.append([n1, n2, n3])
                    count[n2]+=1
            count[n1]+=1
        return ans



nums = [-13,11,11,0,-5,-14,12,-11,-11,-14,-3,0,-3,12,-1,-9,-5,-13,9,-7,-2,9,-1,4,-6,-13,-7,10,10,9,7,13,5,4,-2,7,5,-13,11,10,-12,-14,-5,-8,13,2,-2,-14,4,-8,-6,-13,9,8,6,10,2,6,5,-10,0,-11,-12,12,8,-7,-4,-9,-13,-7,8,12,-14,10,-10,14,-3,3,-15,-14,3,-14,10,-11,1,1,14,-11,14,4,-6,-1,0,-11,-12,-14,-11,0,14,-9,0,7,-12,1,-6]


res = Solution().threeSum(nums)

print(res)