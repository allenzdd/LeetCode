class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_here = max_here = max_so_far = nums[0]
        for x in nums[1:]:
            min_product = min_here * x
            max_product = max_here * x
            min_here = min(min_product, x, max_product)
            max_here = max(max_product, x, min_product)
            max_so_far = max(max_so_far, min_here, max_here)
        return max_so_far






nums = [-1,-2,0,5,-1]
print(Solution().maxProduct(nums))