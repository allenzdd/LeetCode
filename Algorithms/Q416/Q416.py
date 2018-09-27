# DP
# 484 ms
class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:   return False
        target = int(sum_nums / 2)
        opt = [1] + [0] * target
        
        for num in nums:
            # only up to target
            # must backward, because avoid add duplicatition
            for i in range(target-num, -1, -1):
                if opt[i] == 1:
                    opt[i+num] = 1
                if opt[target] == 1:
                    return True
        return False

# 248 ms
# using set
class Solution_st:
    def canPartition(self, nums):
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:   return False
        target = int(sum_nums / 2)
        set_lst = {0}
        for num in nums:
            set_lst.update({(x + num) for x in set_lst})
            if target in set_lst:
                return True
        return False

nums = [1,5,11,5]
print(Solution().canPartition(nums))
            