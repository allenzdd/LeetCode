class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst = list(range(1, len(nums) + 1))
        nums = set(nums)
        res = []
        for x in lst:
            if x not in nums:
                res.append(x)
        return res

nums = [4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers(nums))
            