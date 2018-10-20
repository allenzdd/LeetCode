class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        min_buy = float('inf')
        for i in range(len(prices)):
            sell_temp = prices[i]

            res = max(res, sell_temp - min_buy)

            min_buy = min(min_buy, sell_temp)
            # if min_buy > sell_temp:
            #     min_buy = sell_temp

        return res

if __name__ == "__main__":
    # prices = [7, 1, 5, 3, 6, 4]
    prices = [1, 2]
    print(Solution().maxProfit(prices))


# # TLE
# class Solution:
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         res = 0
#         for i in range(len(prices)):
#             x = prices[i]
#             for j in range(i + 1, len(prices)):
#                 y = prices[j]
#                 res = max(res, y - x)
#         return res
