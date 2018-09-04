class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i]
            else:
                i += 1

        return len(nums)


# class Solution:
#     # @param a list of integers
#     # @return an integer
#     def removeDuplicates(self, A):
#         if not A:
#             return 0

#         newTail = 0

#         for i in range(1, len(A)):
#             if A[i] != A[newTail]:
#                 newTail += 1
#                 A[newTail] = A[i]

#         return newTail + 1


nums = [1, 1, 2, 3, 4]

res = Solution().removeDuplicates(nums)

print(res)
