class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        if nums[right] < target:
            return right + 1
        elif nums[left] > target:
            return left
        else:
            while left <= right - 1:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[left] <= target < nums[mid]:
                    right = mid - 1
                elif nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    break
            if nums[left] > target:
                return left
            elif nums[right] < target:
                return right + 1
            else:
                return (left + right) // 2


# nums = [1, 3, 5, 6]
# target = 5

# nums = [1]
# target = 1

# nums = [1, 2, 4, 6, 7]
# target = 3

# nums = [3, 5, 7, 9, 10]
# target = 8

nums = [1, 3]
target = 3

print(Solution().searchInsert(nums, target))
