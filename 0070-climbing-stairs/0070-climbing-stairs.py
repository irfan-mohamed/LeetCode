class Solution:
    def climbStairs(self, n: int, memo = None) -> int:
        # if memo is None:
        #     memo = {}
        # if n in memo:
        #     return memo[n]
        # if n <= 1:
        #     return 1
        # memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
        
        # return memo[n]

        dp = [0] * (n+1)
        dp[1] = 1
        if n>=2:
            dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]