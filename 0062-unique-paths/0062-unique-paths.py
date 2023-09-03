class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==n==1:
            return 1
        dp=[[1]*m]*n
        for r in range(1,len(dp)):
            for c in range(1,len(dp[r])):
                dp[r][c]=dp[r-1][c]+dp[r][c-1]
        return dp[-1][-1]
        