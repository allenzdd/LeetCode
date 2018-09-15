# DP and Sliding Windows
# 40ms
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # using sliding windows
        hold = float('-inf')
        sold = 0
        rest = 0
        for x in prices:
            pre_sold = sold            
            sold = hold + x
            hold = max(hold, rest - x)
            rest = max(rest, pre_sold)
        return max(rest, sold)



# # Basic DP
# class Solution:
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         n = len(prices)
#         hold = [float('-inf')] * (n+1)
#         sold = [0] * (n+1)
#         rest = [0] * (n+1)

#         for i in range(1, n+1):
#             hold[i] = max(hold[i-1], rest[i-1]-prices[i-1])
#             sold[i] = hold[i-1] + prices[i-1]
#             rest[i] = max(rest[i-1], sold[i-1])
#         return max(sold[-1], rest[-1])

prices = [1,2,3,0,2]
print(Solution().maxProfit(prices))
