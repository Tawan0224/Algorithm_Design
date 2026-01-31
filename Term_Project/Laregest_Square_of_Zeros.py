if matrix[i][j] == 0:
    dp[i][j] = min(
        dp[i-1][j],      # top
        dp[i][j-1],      # left
        dp[i-1][j-1]     # diagonal
    ) + 1
else:
    dp[i][j] = 0