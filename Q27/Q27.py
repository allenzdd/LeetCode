class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1

        return len(nums)


# nums = [3, 2, 2, 3]
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
res = Solution().removeElement(nums, val)
print(res)
