class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for x in nums:
            temp = []
            for res_i in res:
                for i in range(len(res_i) + 1):
                    temp.append(res_i[:i] + [x] + res_i[i:])
            res = temp
            print(x)
            print(res)
        return res


nums = [1, 2, 3, 4]
res = Solution().permute(nums)
print(res)
