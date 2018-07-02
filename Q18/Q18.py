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
            res_temp.append(x)
            res_temp.sort()
            res.append(res_temp)
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
                elif temp < target:
                    j += 1
                elif temp > target:
                    k -= 1
            #     temp = nums[i] + nums[j] + nums[k]
            #     dist_temp = abs(temp - target)
            #     dist_res = abs(res - target)
            #     temp_list = [nums[i], nums[j], nums[k]]
            #     if temp == target:
            #         return temp_list
            #     elif dist_temp < dist_res:
            #         res = temp
            #         res_list = temp_list

            #     if temp < target:
            #         j += 1
            #     elif temp > target:
            #         k -= 1
        return res


nums = [1, 0, -1, 0, -2, 2]
target = 0
res = Solution().threeSumClosest(nums, target)
print(res)
