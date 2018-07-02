class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        for x in nums:
            nums_temp = nums
            nums_temp.remove(x)
            tar_temp = target - x
            res_temp = self.threeSumClosest(nums_temp, tar_temp)
            if res_temp != []:
                [t.append(x) for t in res_temp]
                # res_temp.append(x)
                # print(res_temp)
                # res_temp.sort()
                [t.sort() for t in res_temp]
                [res.append(t) for t in res_temp if t not in res]
        return res

    def threeSumClosest(self, nums, target):
        nums.sort()
        res = []
        # res = sum(nums[0:3])
        # res_list = nums[0:3]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif temp < target:
                    j += 1
                elif temp > target:
                    k -= 1
        return res


# nums = [1, 0, -1, 0, -2, 2]
# nums = [-3, -2, -1, 0, 0, 1, 2, 3]
nums = [-5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5]

target = 0
res = Solution().fourSum(nums, target)
print(res)
