class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for x in nums:
            # print(x)
            temp = []
            for res_i in res:
                for i in range(len(res_i) + 1):
                    # print(len(res_i))
                    temp.append(res_i[:i] + [x] + res_i[i:])
                    # print(temp)
            res = temp
            print(res)
        return res


nums = [1, 2, 3, 4]
res = Solution().permute(nums)
print(res)
