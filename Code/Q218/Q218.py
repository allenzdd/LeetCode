class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        left_head = [[x[0], x[2]] for x in buildings]
        right_bottom = [[x[1], -x[2]] for x in buildings]

