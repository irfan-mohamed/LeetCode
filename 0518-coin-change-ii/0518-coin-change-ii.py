class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        if not coins or amount == 0:
            return 1 if amount == 0 else 0
        dp = [[0] * (amount+1) for _ in range(len(coins))]
        for i in range(len(coins)):
            for j in range(amount+1):
                dp[i][0] = 1
                if coins[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-coins[i]]
        return dp[-1][-1]