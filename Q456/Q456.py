class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(0, len(nums) - 2):
            temp = nums.copy().remove(nums[i])
            temp.sort()
            temp_max = max(temp)
            for j in range(0, len(temp) - 1):
                if temp[j] > nums[i]:
                    if temp[j] == temp_max:
                        temp2 =
        return False


# nums = [1, 3, 2, 4]
# nums = [1, 2, 3, 4]
# nums = [3, 1, 4, 2]
# nums = [-1, 3, 2, 0]
nums = [3, 5, 0, 3, 4]
res = Solution().find132pattern(nums)
print(res)
