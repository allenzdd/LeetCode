# DFS
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        self.res_min = float('inf')
        self.dfs(coins, 0, amount, 0)
        return -1 if self.res_min == float('inf') else self.res_min
    
    def dfs(self, coins, start, amount, count):
        if amount == 0:
            self.res_min = count
            return
        if start == len(coins): return
        n = coins[start]
        for k in range(amount // n, -1, -1):
            if k + count >= self.res_min:    break
            self.dfs(coins, start+1, amount-n*k, count+k)




# # DP
# class Solution:
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         # using sliding windows
#         opt = [0] + [float('inf')] * amount
        
#         for coin in coins:
#             for j in range(coin, amount+1):
#                 # similar with opt[j] = min(opt[j], opt[j-coin]+1)
#                 if opt[j] <= opt[j-coin]:
#                     continue
#                 opt[j] = opt[j-coin] + 1
#         return -1 if opt[-1] == float('inf') else opt[-1]


coins = [1,2,5]
amount = 11
print(Solution().coinChange(coins, amount))