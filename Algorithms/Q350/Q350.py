class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = set(nums1) & set(nums2)
        res = []
        for x in intersection:
            count = min(nums1.count(x), nums2.count(x))
            res.extend([x] * count)
        return res

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(Solution().intersect(nums1, nums2))