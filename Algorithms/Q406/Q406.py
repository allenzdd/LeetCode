# [[7,0]] (insert [7,0] at index 0)
# [[7,0],[7,1]] (insert [7,1] at index 1)
# [[7,0],[6,1],[7,1]] (insert [6,1] at index 1)
# [[5,0],[7,0],[6,1],[7,1]] (insert [5,0] at index 0)
# [[5,0],[7,0],[5,2],[6,1],[7,1]] (insert [5,2] at index 2)
# [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] (insert [4,4] at index 4)
# 168ms
# O(n^2)
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:  return []
        peo_sorted = sorted(people, key=lambda x: (-x[0], x[1]))
        res = [peo_sorted[0]]
        for h, k in peo_sorted[1:]:
            res.insert(k, [h, k])
        return res



people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(Solution().reconstructQueue(people))