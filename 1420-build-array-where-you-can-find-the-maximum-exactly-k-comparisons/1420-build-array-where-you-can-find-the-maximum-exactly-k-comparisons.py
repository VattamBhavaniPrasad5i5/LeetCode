class Solution(object):
    def numOfArrays(self, n, m, k):
        MOD = 10 ** 9 + 7
        dp = [[[0] * m for _ in range(k)] for _ in range(n)]
        
        for i in range(m):
            dp[0][0][i] = 1
        
        for i in range(1, n):
            for cost in range(min(i + 1, k)):
                for maxVal in range(m):
                    total = dp[i - 1][cost][maxVal] * (maxVal + 1) % MOD
                    
                    if cost != 0:
                        for prevMax in range(maxVal):
                            total = (total + dp[i - 1][cost - 1][prevMax]) % MOD
                    
                    dp[i][cost][maxVal] = total
        
        ans = 0
        for maxVal in range(m):
            ans = (ans + dp[n - 1][k - 1][maxVal]) % MOD
        
        return ans
        