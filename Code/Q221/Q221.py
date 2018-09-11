class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        opt = [[0 if matrix[i][j] == '0' else 1 for j in range(n)] for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    opt[i][j] = min(opt[i-1][j], opt[i][j-1], opt[i-1][j-1]) + 1
                else:
                    opt[i][j] = 0
        
        length = max(max(row)for row in opt)

        return length ** 2


    #     max_area = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if matrix[i][j] == '1':
    #                 area = self.max_square_area(i, j, matrix, m, n)
    #                 max_area = max(area, max_area)
        
    #     return max_area

    # def max_square_area(self, i, j, matrix, m, n):
    #     area = 1
    #     length_max = min(m - i, n - j)
    #     for p in range(1, length_max):
    #         if matrix[i + p][j + p] == '1' and matrix[i + p][j] == '1' and matrix[i][j + p] == '1':
    #             area += 1 * 3
    #         else:
    #             break
    #     return area  




# mat = [["1","0","1","0","0"],
#         ["1","0","1","1","1"],
#         ["1","1","1","1","1"],
#         ["1","0","0","1","0"]]

mat = [["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]

print(Solution().maximalSquare(mat))