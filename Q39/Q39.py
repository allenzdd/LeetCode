class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return
        else:
            for i in range(index, len(nums)):
                self.dfs(nums, target - nums[i], i, path + [nums[i]], res)


candidates = [2, 3, 6, 7]
target = 7

print(Solution().combinationSum(candidates, target))
