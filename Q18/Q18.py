class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        # nums_ = nums
        for x in nums:
            nums_temp = nums[:]
            nums_temp.remove(x)
            tar_temp = target - x
            res_temp = self.threeSum(nums_temp, tar_temp)
            # print(res_temp)
            if res_temp != []:
                [t.append(x) for t in res_temp]
                # res_temp.append(x)
                # print(res_temp)
                # res_temp.sort()
                [t.sort() for t in res_temp]
                [res.append(t) for t in res_temp if t not in res]
            nums_temp = []
            res_temp = []
        return res

    def threeSum(self, nums, target):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            if target > nums[k] * 3 or target < nums[i] * 3:
                continue
            else:
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
# nums = [-5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5]
# nums = [-5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5]
nums = [1, -2, -5, -4, -3, 3, 3, 5]
# nums = [-495,-482,-455,-447,-400,-388,-381,-360,-350,-340,-330,-317,-308,-300,-279,-235,-209,-206,-188,-186,-171,-145,-143,-141,-137,-129,-121,-115,-97,-56,-47,-28,-20,-19,8,11,35,41,46,50,69,84,85,86,88,91,135,160,171,172,177,190,226,234,238,244,249,253,254,272,281,284,294,296,300,303,307,313,320,320,327,334,355,362,367,401,426,436,456,467,473,473,484]


# target = 0
target = -11
# target = -7178

res = Solution().fourSum(nums, target)
print(res)
