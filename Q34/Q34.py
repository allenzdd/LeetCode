class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid
                right = mid
                while nums[left] == target and nums[right] == target:
                    if left - 1 >= 0 and nums[left - 1] == target:
                        left -= 1
                    elif right + 1 <= len(nums) - 1 and nums[right + 1] == target:
                        right += 1
                    else:
                        break
                return left, right
            elif nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return [-1, -1]


# nums = [5, 7, 7, 8, 8, 10]
# target = 8

# nums = [1]
# target = 1

nums = [2, 2]
target = 2

print(Solution().searchRange(nums, target))
