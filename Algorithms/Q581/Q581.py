class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre_num = nums[0]
        end = 0
        for i in range(1, len(nums)):
            if nums[i] < pre_num:
                end = i
            else:
                pre_num = nums[i]
        
        post_num = nums[-1]   
        start = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > post_num:
                start = i
            else:
                post_num = nums[i]
        if start == end:    return 0
        return max(end - start + 1, 0)



# nums = [2, 6, 4, 8, 10, 9, 15]
# nums = [1,2,3,4]
# nums = [1]
nums = [1,3,2,2,2]
# nums = [1,3,2,3,3]
print(Solution().findUnsortedSubarray(nums))