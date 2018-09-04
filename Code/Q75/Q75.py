class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        else:
            i, j, pin = 0, len(nums) - 1, 0
            while i <= j:
                if nums[i] == 1:
                    i += 1
                elif nums[i] == 2:
                    while i < j and nums[j] == 2:
                        j -= 1

                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
                else:
                    nums[i], nums[pin] = nums[pin], nums[i]
                    i += 1
                    pin += 1


# nums = [2, 0, 2, 1, 1, 0]
# nums = [2, 0, 1]

Solution().sortColors(nums)

print(nums)
