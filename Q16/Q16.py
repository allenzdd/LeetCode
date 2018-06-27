class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1

        nsort = sorted(count.keys())

        if len(nsort) == 1:
            return nsort[0] * 3
        elif len(nsort) == 2:
            n1 = nsort[0]
            n2 = nsort[1]
            if count[n1] >= 2 and count[n2] == 1:
                temp_sum = n1 * 2 + n2
                return temp_sum
            elif count[n1] == 1 and count[n2] >= 2:
                temp_sum = n1 + n2 * 2
                return temp_sum
            else:
                temp_sum1 = n1 * 2 + n2
                temp_sum2 = n1 + n2 * 2
                if abs(target - temp_sum1) < abs(target - temp_sum2):
                    return temp_sum1
                else:
                    return temp_sum2
        else:
            temp_close = abs(max(nsort))

            for i in range(len(nsort)):
                n1 = nsort[i]
                if count[n1] >= 1:
                    count[n1] -= 1
                    for j in range(i + 1, len(nsort)):
                        n2 = nsort[j]
                        if count[n2] >= 1:
                            count[n2] -= 1
                            for k in range(j + 1, len(nsort)):
                                n3 = nsort[k]
                                if count[n3] >= 1:
                                    count[n3] -= 1
                                    temp_sum = n1 + n2 + n3
                                    temp = abs(target - temp_sum)
                                    if temp < temp_close:
                                        temp_close = temp
                                        res = temp_sum
                                count[n3] += 1
                        count[n2] += 1
                count[n1] += 1
            return res


# nums = [-1, 2, 1, -4, 2, 6]
# nums = [0, 0, 0]
nums = [1, 2, 3]
target = 1

res = Solution().threeSumClosest(nums, target)

print(res)
