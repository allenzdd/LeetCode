class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        k = (n1 + n2 + 1) / 2
        l, r = 0, n1

        while l < r:
            m1 = int(l + (r-l) / 2)
            m2 = int(k - m1)
            if nums1[m1] < nums2[m2-1]:
                l = m1+1
            else:
                r = m1
        
        m1 = int(l)
        m2 = int(k - l)

        c1 = max(
            nums1[m1-1] if m1 > 0 else float('-inf'),
            nums2[m2-1] if m2 > 0 else float('-inf')
        ) 

        if (n1 + n2) % 2 == 1:
            return c1
        
        c2 = min(
            nums1[m1] if m1 < n1 else float('inf'),
            nums2[m2] if m2 < n2 else float('inf')
        ) 

        return (c1+c2) / 2


if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2]
    res = Solution().findMedianSortedArrays(nums1, nums2)
    print(res)