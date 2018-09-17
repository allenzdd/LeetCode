class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        res = [dic[i][0] for i in range(k)]
        return res


nums = [1,1,1,2,2,3]
print(Solution().topKFrequent(nums, 2))