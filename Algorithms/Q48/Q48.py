class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for l in range(n // 2):
            r = n - l - 1
            for p in range(l, r):
                q = n - p - 1
                temp = matrix[l][p]
                matrix[l][p] = matrix[q][l]
                matrix[q][l] = matrix[r][q]
                matrix[r][q] = matrix[p][r]
                matrix[p][r] = temp
        return matrix


# #Zip Method
# class Solution:
#     def rotate(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: void Do not return anything, modify matrix in-place instead.
#         """
#         #res = matrix.copy()
#         # zipped = zip(matrix[::-1])
#         matrix[::] = zip(*matrix[::-1])
#         #return res


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
res = Solution().rotate(matrix)
print(res)
