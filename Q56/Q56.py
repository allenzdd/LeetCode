# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        for interval in sorted(intervals, key=lambda s: s.start):
            if not res or interval.start > res[-1].end:
                res.append(interval)
            else:
                res[-1].end = max(interval.end, res[-1].end)
        return res


inp = [[1, 3], [2, 6], [8, 10], [15, 18]]

print(Solution().merge(inp))
