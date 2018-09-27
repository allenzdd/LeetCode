class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        zero_location = []
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                zero_location.append(i)

        while (len(zero_location) > 0):
            is_beyond = False
            current_zero_location = zero_location.pop()
            for i in range(1, current_zero_location + 1):
                if nums[current_zero_location - i] > i:
                    is_beyond = True
                    break
            if is_beyond is False:
                return False

        return True


# Input = [2, 3, 1, 1, 4]
# Input = [3, 2, 1, 0, 4]
# Input = [0]
Input = [2, 0, 0]

print(Solution().canJump(Input))
